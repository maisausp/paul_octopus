import importlib

from predictor.AbstractPredictor import AbstractPredictor

from flask import Flask, send_from_directory

#from utils.azure_storage import download_file_from_azure
from utils.csv import *

PATH_FILE = "/home/maisa/Documentos/ciandt/paul_octopus/paul-octopus-python_submited/"
app = Flask(__name__)

@app.route("/")
def index():
    return "Paul the Octopus is alive!!!"


@app.route("/predict/<predictor_name>/<phase>")
def predict(predictor_name, phase):

    # Download all the files that you need for your predictors
    #download_file_from_azure(container_name='files', blob_name='historical-results.csv')
    #download_file_from_azure(container_name='files', blob_name='sample_predictions_submission.csv')

    phase = int(phase)

    # Use a sample file to load all matches
    if phase == 1:
        matches = read_csv(PATH_FILE + 'sample_predictions_submission.csv')
    if phase == 2:
        matches = read_csv(PATH_FILE + 'sample_predictions_submission_phase2.csv')
    if phase == 3:
        matches = read_csv(PATH_FILE + 'sample_predictions_submission_phase3.csv')
    if phase == 4:
        matches = read_csv(PATH_FILE + 'sample_predictions_submission_phase4.csv')
    if phase == 5:
        matches = read_csv(PATH_FILE + 'sample_predictions_submission_phase5.csv')

    # Instantiate the Predictor class based on the predictor_name
    PredictorClass = getattr(importlib.import_module(f'predictor.{predictor_name}'), predictor_name)
    predictor: AbstractPredictor = PredictorClass()

    # Make predictions and write them into the predictions.csv file
    predictions = predictor.predict(matches)
    write_csv(predictions, ['home', 'home_score', 'away_score', 'away'], PATH_FILE + 'predictions.csv')

    # Return the predictions.csv file for downloading
    return send_from_directory('.', 'predictions.csv')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)


