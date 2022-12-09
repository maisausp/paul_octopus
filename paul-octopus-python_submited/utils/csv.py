import csv
import pandas as pd

PATH_FILE = "/home/maisa/Documentos/ciandt/paul_octopus/paul-octopus-python_submited/"

def read_historical_results():
    
    historical_results = pd.read_csv(PATH_FILE + 'historical-results.csv')
    return historical_results[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'tournament']]

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        matches_data = [row for row in reader]

    return matches_data


def write_csv(data, csv_columns, file_name):
    with open(file_name, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, delimiter=',', fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(data)
