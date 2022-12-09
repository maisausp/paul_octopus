from datetime import datetime
import constants.params as global_params
from dateutil.relativedelta import relativedelta

def extract_past_games_of_participants(p_raw_dataset, p_wc_dataset):
  '''
  Extraí os jogos anteriores ao parametro 'p_data_initial' que seja entre duas seleções presentes nos parametros 'p_wc_dataset'.
  O retorno é ordenado pela data da partida em ordem descendente.
  '''
  
  games_before = p_raw_dataset[(p_raw_dataset['date'] < p_wc_dataset[0])]  
  
  games_of_participants = games_before[games_before['home_team'].apply(lambda x: x in p_wc_dataset[1])]
  games_of_participants = games_of_participants[games_of_participants['away_team'].apply(lambda x: x in p_wc_dataset[1])]
  
  games_of_participants = games_of_participants.sort_values(by='date',ascending=False)

  return games_of_participants

def extract_past_year_games_of_participants(p_raw_dataset, p_wc_dataset):
  '''
  Extraí os jogos anteriores ao parametro 'p_data_initial' que seja entre duas seleções presentes nos parametros 'p_wc_dataset'.
  O retorno é ordenado pela data da partida em ordem descendente.
  '''
  
  v_kick_off_date = datetime.strptime(p_wc_dataset[0], '%Y-%m-%d')
  
  games_before = p_raw_dataset[(p_raw_dataset['date'] < p_wc_dataset[0])]  
  games_before_one_year = games_before[(games_before['date'] > (v_kick_off_date - relativedelta(years=global_params.C_EXTRACT_YEARS)).strftime('%Y-%m-%d'))]  
  
  games_of_participants = games_before_one_year[games_before_one_year['home_team'].apply(lambda x: x in p_wc_dataset[1])]
  games_of_participants = games_of_participants[games_of_participants['away_team'].apply(lambda x: x in p_wc_dataset[1])]
  
  games_of_participants = games_of_participants.sort_values(by='date',ascending=False)

  return games_of_participants

def extract_past_year_games(p_raw_dataset, p_wc_dataset):
  '''
  Extraí os jogos anteriores ao parametro 'p_data_initial' que seja entre duas seleções presentes nos parametros 'p_wc_dataset'.
  O retorno é ordenado pela data da partida em ordem descendente.
  '''
  
  v_kick_off_date = datetime.strptime(p_wc_dataset[0], '%Y-%m-%d')
  
  games_before = p_raw_dataset[(p_raw_dataset['date'] < p_wc_dataset[0])]  
  games_before_one_year = games_before[(games_before['date'] > (v_kick_off_date - relativedelta(years=global_params.C_EXTRACT_YEARS)).strftime('%Y-%m-%d'))]    
  
  games_before_one_year = games_before_one_year.sort_values(by='date',ascending=False)

  return games_before_one_year

def extract_wc_games_by_edition(p_raw_data, p_kick_off_date):

  '''
  Extraí as partidas do tipo de torneio 'World Cup' que aconteceram no mesmo ano infomado pelo parametro 'p_kick_off_date'.
  '''
  v_kick_off_date = datetime.strptime(p_kick_off_date, '%Y-%m-%d')
  v_wc_games = p_raw_data[(p_raw_data['date'].dt.strftime('%Y') == v_kick_off_date.strftime('%Y'))]  
  v_wc_games = v_wc_games[(v_wc_games['tournament'] == global_params.C_TOURNAMENT)]  

  return v_wc_games

def select_interesting_columns(p_raw_dataset):
  return p_raw_dataset[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'tournament']]
