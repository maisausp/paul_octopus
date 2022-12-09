from predictor.AbstractPredictor import AbstractPredictor
import numpy as np
import utils.global_variables as global_variables

class MPLPredictor(AbstractPredictor):

    def predict_match(self, home, away):
        X_test = v_dataset = np.zeros((1,10))

        X_test[0,:5] = global_variables.participants_score[home]
        X_test[0,5:] = global_variables.participants_score[away]
        prediction_home_score = global_variables.model.predict(X_test)

        X_test[0,:5] = global_variables.participants_score[away]
        X_test[0,5:] = global_variables.participants_score[home]
        prediction_away_score = global_variables.model.predict(X_test)

        return {'home': home, 'home_score': int(prediction_home_score[0]), 'away_score': int(prediction_away_score[0]), 'away': away}
