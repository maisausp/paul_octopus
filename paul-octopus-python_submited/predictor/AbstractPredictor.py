from abc import ABC, abstractmethod
from utils.csv import *
import utils.global_variables as global_variables
from pre_processing.pre_processing_data import *
from joblib import load
from utils.team_aliases import normalize_team_name
from utils.paths import get_model_file

class AbstractPredictor(ABC):

    @abstractmethod
    def predict_match(self, home, away):
        print(f'predicting {home} x {away}')
        pass

    def predict(self, matches):

        predictions = []
        global_variables.participants_score = dict()
        raw_data = read_historical_results()
        global_variables.model = load(get_model_file())
        participants = set()

        for match in matches:
            participants.add(normalize_team_name(match['home']))
            participants.add(normalize_team_name(match['away']))
        
        games_of_participants = raw_data[raw_data['home_team'].apply(lambda x: normalize_team_name(x) in participants)]
        games_of_participants = games_of_participants[games_of_participants['away_team'].apply(lambda x: normalize_team_name(x) in participants)]
        filtered_data = games_of_participants.sort_values(by='date', ascending=False)

        for match in matches:
            team_home = match['home']
            team_away = match['away']
            team_home_fix = normalize_team_name(team_home)
            team_away_fix = normalize_team_name(team_away)

            if team_home not in global_variables.participants_score.keys():
                global_variables.participants_score[team_home] = get_participant_score_from_games(team_home_fix, filtered_data, len(participants))
            if team_away not in global_variables.participants_score.keys():
                global_variables.participants_score[team_away] = get_participant_score_from_games(team_away_fix, filtered_data, len(participants))
            predictions.append(self.predict_match(team_home, team_away))

        return predictions
