from abc import ABC, abstractmethod
from utils.csv import *
import utils.global_variables as global_variables
from pre_processing.pre_processing_data import *
from joblib import load
PATH_FILE = "/home/maisa/Documentos/ciandt/paul_octopus/paul-octopus-python_submited/"

class AbstractPredictor(ABC):

    @abstractmethod
    def predict_match(self, home, away):
        print(f'predicting {home} x {away}')
        pass

    def predict(self, matches):

        predictions = []
        global_variables.participants_score = dict()
        raw_data = read_historical_results()
        global_variables.model = load(PATH_FILE + 'MLPClassifier.h5')
        participants = set()

        for match in matches:
            participants.add(match['home'])
            participants.add(match['away'])
        
        list_participants = str(matches) + 'United States' # Adição para tratamento de diferença de nomenclatura de seleções

        games_of_participants = raw_data[raw_data['home_team'].apply(lambda x: x in list_participants)]
        games_of_participants = games_of_participants[games_of_participants['away_team'].apply(lambda x: x in list_participants)]
        filtered_data = games_of_participants.sort_values(by='date', ascending=False)

        for match in matches:
            team_home = team_home_fix = match['home']
            team_away = team_away_fix = match['away']

            if team_home == 'USA':
                team_home_fix = 'United States'
            if team_away == 'USA':
                team_away_fix = 'United States'


            if team_home not in global_variables.participants_score.keys():
                global_variables.participants_score[team_home] = get_participant_score_from_games(team_home_fix, filtered_data, len(participants))
            if team_away not in global_variables.participants_score.keys():
                global_variables.participants_score[team_away] = get_participant_score_from_games(team_away_fix, filtered_data, len(participants))
            predictions.append(self.predict_match(team_home, team_away))

        return predictions
