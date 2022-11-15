import numpy as np
import constants.params as global_params

def update_score_statistics(p_team_score, p_opponent_score, p_score_statistics):
  '''
  Atualiza o array de entrada 'p_score_statistics' com estatíticas de gols feitos; gols sofridos e número de empates.
  Formato do array: size = 3, [0] = Número de gols feitos; [1] = Número de gols sofridos; [2] = Número de empates.
  '''
  p_score_statistics[0] = p_score_statistics[0] + p_team_score
  p_score_statistics[1] = p_score_statistics[1] + p_opponent_score

  if p_team_score == p_opponent_score and global_params.C_EXTRACT_NR_EMPATES:
    p_score_statistics[2] = p_score_statistics[2] + 1

  if p_team_score > p_opponent_score and global_params.C_EXTRACT_NR_VICTORIES:
    p_score_statistics[3] = p_score_statistics[3] + 1

  if p_team_score < p_opponent_score and global_params.C_EXTRACT_NR_LOSES:
    p_score_statistics[4] = p_score_statistics[4] + 1

  return p_score_statistics

def get_nr_features_by_participant():
  
  if global_params.C_EXTRACT_NR_LOSES:
    return 5
  if global_params.C_EXTRACT_NR_VICTORIES:
    return 4
  if global_params.C_EXTRACT_NR_EMPATES:
    return 3
  
  return 2


def get_participant_score_from_games(p_participant, p_games):

  '''
  Extraí o score do participante definido no parametro 'p_participant' conforme conjuto de partidas em 'p_games'.
  '''

  i = j = 0
  
  v_features = np.zeros(get_nr_features_by_participant())
  
  # As estatísticas são extraídas de até C_NR_PARTICIPANTS partidas.
  while j < global_params.C_NR_PARTICIPANTS and i < p_games.shape[0]:  
    
    v_home_team = p_games.iloc[i][1]
    v_away_team = p_games.iloc[i][2]
    v_home_team_score = p_games.iloc[i][3]
    v_away_team_score = p_games.iloc[i][4]

    if p_participant == v_home_team:      
      v_features = update_score_statistics(v_home_team_score, v_away_team_score, v_features)
      j = j + 1

    if p_participant == v_away_team:      
      v_features = update_score_statistics(v_away_team_score, v_home_team_score, v_features)      
      j = j + 1

    i = i + 1

  return v_features