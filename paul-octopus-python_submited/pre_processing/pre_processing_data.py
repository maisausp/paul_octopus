import numpy as np


def update_score_statistics(p_team_score, p_opponent_score, p_score_statistics):
  '''
  Atualiza o array de entrada 'p_score_statistics' com estatíticas de gols feitos; gols sofridos e número de empates.
  Formato do array: size = 3, [0] = Número de gols feitos; [1] = Número de gols sofridos; [2] = Número de empates.
  '''
  p_score_statistics[0] = p_score_statistics[0] + p_team_score
  p_score_statistics[1] = p_score_statistics[1] + p_opponent_score

  if p_team_score == p_opponent_score:
    p_score_statistics[2] = p_score_statistics[2] + 1

  if p_team_score > p_opponent_score:
    p_score_statistics[3] = p_score_statistics[3] + 1

  if p_team_score < p_opponent_score:
    p_score_statistics[4] = p_score_statistics[4] + 1

  return p_score_statistics



def get_participant_score_from_games(p_participant, p_historical_games, p_max_games = None):

  '''
  Extrai o score do participante definido no parametro 'p_participant' conforme conjuto de partidas em 'p_historical_games'.
  '''

  v_nr_features_participant = 5
  i = j = 0
  
  v_features = np.zeros(v_nr_features_participant)
  v_max_games = p_max_games if p_max_games is not None else p_historical_games.shape[0]
  
  while j < v_max_games and i < p_historical_games.shape[0]:  
    
    v_home_team = p_historical_games.iloc[i][1]
    v_away_team = p_historical_games.iloc[i][2]
    v_home_team_score = p_historical_games.iloc[i][3]
    v_away_team_score = p_historical_games.iloc[i][4]

    if p_participant == v_home_team:      
      v_features = update_score_statistics(v_home_team_score, v_away_team_score, v_features)
      j = j + 1

    if p_participant == v_away_team:      
      v_features = update_score_statistics(v_away_team_score, v_home_team_score, v_features)      
      j = j + 1

    i = i + 1

  return v_features
