import selection_data.extractor as extractor
import calculation_features.score as calculator
import constants.params as global_params
import constants.team_aliases as team_aliases
import numpy as np

C_LEGACY_TRAIN_WC_EDITIONS = [
  global_params.C_2002_WC,
  global_params.C_2006_WC,
  global_params.C_2010_WC,
  global_params.C_2014_WC,
]

C_TRAIN_WC_EDITIONS_FOR_2026_VALIDATION = [
  global_params.C_2002_WC,
  global_params.C_2006_WC,
  global_params.C_2010_WC,
  global_params.C_2014_WC,
  global_params.C_2018_WC,
]

C_TEST_WC_EDITION_FOR_2026 = global_params.C_2022_WC
C_TEST_WC_EDITION_FALLBACK = global_params.C_2018_WC
C_PREDICTION_WC_EDITION = global_params.C_2026_WC

def compile_features_by_world_cup_edition(p_raw_dataset, p_wc_dataset):
  
  '''
  Extraí as features de todos os participantes presentes no parametro 'p_wc_dataset[1]' de partidas anteriores ao parametro 'p_wc_dataset[0]' conforme conjunto de 
  partidas fornecido pelo parametro 'p_raw_dataset'.
  '''
  v_wc_dataset = [p_wc_dataset[0], team_aliases.normalize_team_names(p_wc_dataset[1])]

  if(global_params.C_EXTRACT_32_or_1_year):
    if(global_params.C_EXTRACT_JUST_PARTICIPANTS):
      v_past_games_of_participants = extractor.extract_past_year_games_of_participants(p_raw_dataset, v_wc_dataset)
    else:
      v_past_games_of_participants = extractor.extract_past_year_games(p_raw_dataset, v_wc_dataset)
  else:
    v_past_games_of_participants = extractor.extract_past_games_of_participants(p_raw_dataset, v_wc_dataset)

  v_features = dict()
  
  v_nr_participants = len(v_wc_dataset[1])

  for participant in v_wc_dataset[1]:
    v_features[participant] = calculator.get_participant_score_from_games(participant, v_past_games_of_participants, v_nr_participants)
  
  v_nr_features_by_sample = 2*calculator.get_nr_features_by_participant()
  return v_features, v_nr_features_by_sample


def insert_sample_into_dataset(p_index, p_features_A, p_features_B, p_score_A, p_out_dataset):

  '''
  Insere uma amostra no dataset informado pelo parametro 'p_out_dataset'. A amostra será posicionada no índice informado pelo parametro 'p_index' e 
  ela será composta pelos dados do parametro 'p_features_A', seguidos pelos dados do parametro de 'p_features_B', que serão seguidos pelos dados do parametro 'p_score_A'.
  '''
  v_nr_features = p_features_A.shape[0]
  p_out_dataset[p_index, 0:v_nr_features] = p_features_A
  p_out_dataset[p_index, v_nr_features:(2*v_nr_features)] = p_features_B
  p_out_dataset[p_index, -1] = p_score_A


def compile_dataset (p_cup_games, p_features, p_nr_features_by_sample):

  '''
  Para cada partida de copa do mundo informada no parametro 'p_cup_games' são calculadas as features da seleção A e da seleção B.
  Na sequência duas amostras são inseridas no dataset: 
    1a: feature seleação A, feature seleção B, número de gols de A
    1a: feature seleação B, feature seleção A, número de gols de B
  '''
  v_dataset = np.zeros((2 * p_cup_games.shape[0], p_nr_features_by_sample + 1))

  for i in range(p_cup_games.shape[0]):      

    v_home_team = team_aliases.normalize_team_name(p_cup_games.iloc[i][1])
    v_away_team = team_aliases.normalize_team_name(p_cup_games.iloc[i][2])
    v_home_team_score = p_cup_games.iloc[i][3]
    v_away_team_score = p_cup_games.iloc[i][4]
    
    v_features_home_team = p_features[v_home_team]
    v_features_away_team = p_features[v_away_team]

    insert_sample_into_dataset((2*i), v_features_home_team, v_features_away_team, v_home_team_score, v_dataset)
    insert_sample_into_dataset((2*i)  + 1, v_features_away_team, v_features_home_team, v_away_team_score, v_dataset)

  return v_dataset

def extract_dataset_by_cup(p_raw_dataset, p_world_cup_edition_dataset):

  '''
  Obtém o dataset para a edição da copa informada pelo parametro 'p_world_cup_edition_dataset'. Para cálculo da features são usados os dados originais do parametro 'p_raw_dataset'.
  '''
  v_world_cup_edition_dataset = [p_world_cup_edition_dataset[0], team_aliases.normalize_team_names(p_world_cup_edition_dataset[1])]
  v_cup_edition_games = extractor.extract_wc_games_by_edition(p_raw_dataset, v_world_cup_edition_dataset[0])
  v_features_by_cup_edition, v_nr_features_by_sample = compile_features_by_world_cup_edition(p_raw_dataset, v_world_cup_edition_dataset)  
  v_cup_edition_dataset = compile_dataset(v_cup_edition_games, v_features_by_cup_edition, v_nr_features_by_sample)

  return v_cup_edition_dataset

def extract_dataset_by_cups(p_raw_dataset, p_world_cup_editions):
  
  v_datasets = [extract_dataset_by_cup(p_raw_dataset, v_world_cup_edition) for v_world_cup_edition in p_world_cup_editions]
  return np.concatenate(v_datasets, axis=0)

def has_world_cup_games(p_raw_dataset, p_world_cup_edition_dataset):

  v_games = extractor.extract_wc_games_by_edition(p_raw_dataset, p_world_cup_edition_dataset[0])
  return v_games.shape[0] > 0

def get_train_test_data_sets(p_raw_dataset, p_train_wc_editions = C_TRAIN_WC_EDITIONS_FOR_2026_VALIDATION, p_test_wc_edition = C_TEST_WC_EDITION_FOR_2026, p_prediction_wc_edition = C_PREDICTION_WC_EDITION):
  
  p_raw_dataset = extractor.select_interesting_columns(p_raw_dataset)

  if has_world_cup_games(p_raw_dataset, p_test_wc_edition):
    dataset_train = extract_dataset_by_cups(p_raw_dataset, p_train_wc_editions)
    dataset_test = extract_dataset_by_cup(p_raw_dataset, p_test_wc_edition)
  else:
    dataset_train = extract_dataset_by_cups(p_raw_dataset, C_LEGACY_TRAIN_WC_EDITIONS)
    print('Aviso: dataset de teste solicitado não encontrado no histórico. Usando treino 2002-2014 e teste 2018.')
    dataset_test = extract_dataset_by_cup(p_raw_dataset, C_TEST_WC_EDITION_FALLBACK)

  features_prediction, _ = compile_features_by_world_cup_edition(p_raw_dataset, p_prediction_wc_edition)

  return dataset_train, dataset_test, features_prediction

def set_score_threshold(v_dataset, v_th_min = 0, v_th_max = 10):
  
  y_clip =  np.clip(v_dataset[:, -1], v_th_min, v_th_max, v_dataset[:, -1])
  return v_dataset

def remove_equal_greater_score(v_dataset, v_score):

  return v_dataset[v_dataset[:, -1] < v_score]
