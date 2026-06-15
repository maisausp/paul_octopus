import importlib

from predictor.AbstractPredictor import AbstractPredictor

from flask import Flask, abort, send_from_directory

#from utils.azure_storage import download_file_from_azure
from utils.csv import *
from utils.paths import APP_DIR, get_data_file

app = Flask(__name__)

PHASE_FILES = {
    1: 'sample_predictions_submission.csv',
    2: 'sample_predictions_submission_phase2.csv',
    3: 'sample_predictions_submission_phase3.csv',
    4: 'sample_predictions_submission_phase4.csv',
    5: 'sample_predictions_submission_phase5.csv',
}

@app.route("/")
def index():
    return "Paul the Octopus is alive!!!"


@app.route("/predict/<predictor_name>")
def predict_default_phase(predictor_name):
    return predict(predictor_name, 1)


@app.route("/predict/<predictor_name>/<phase>")
def predict(predictor_name, phase):

    # Download all the files that you need for your predictors
    #download_file_from_azure(container_name='files', blob_name='historical-results.csv')
    #download_file_from_azure(container_name='files', blob_name='sample_predictions_submission.csv')

    phase = int(phase)
    matches_file_name = PHASE_FILES.get(phase)

    if matches_file_name is None:
        abort(404, description='Invalid phase')

    matches_file = get_data_file(matches_file_name)

    if not matches_file.exists():
        abort(404, description='Matches file not found')

    matches = read_csv(matches_file)

    # Instantiate the Predictor class based on the predictor_name
    PredictorClass = getattr(importlib.import_module(f'predictor.{predictor_name}'), predictor_name)
    predictor: AbstractPredictor = PredictorClass()

    # Make predictions and write them into the predictions.csv file
    predictions = predictor.predict(matches)
    write_csv(predictions, ['home', 'home_score', 'away_score', 'away'], APP_DIR / 'predictions.csv')

    # Return the predictions.csv file for downloading
    return send_from_directory(APP_DIR, 'predictions.csv')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

