import csv
import os
import pandas as pd
from utils.paths import APP_DIR, get_data_file


def read_historical_results():

    historical_path = get_data_file('results.csv')

    if not historical_path.exists():
        historical_path = get_data_file('historical-results.csv')

    historical_results = pd.read_csv(historical_path, parse_dates=['date'])
    historical_results = historical_results.dropna(subset=['home_score', 'away_score'])
    cutoff_date = os.environ.get('PAUL_OCTOPUS_CUTOFF_DATE', '2026-06-11')
    historical_results = historical_results[historical_results['date'] < pd.Timestamp(cutoff_date)]
    historical_results['home_score'] = historical_results['home_score'].astype(int)
    historical_results['away_score'] = historical_results['away_score'].astype(int)
    return historical_results[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'tournament']]

def read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        matches_data = [row for row in reader]

    return matches_data


def write_csv(data, csv_columns, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as fp:
        writer = csv.DictWriter(fp, delimiter=',', fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(data)
