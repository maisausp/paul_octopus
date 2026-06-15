import pandas as pd
import numpy as np
import ast


def read_historical_results(p_path = 'paul-octopus-2026/results.csv'):
    
    historical_results = pd.read_csv(p_path, parse_dates = ['date'])
    historical_results = historical_results.dropna(subset=['home_score', 'away_score'])
    historical_results['home_score'] = historical_results['home_score'].astype(int)
    historical_results['away_score'] = historical_results['away_score'].astype(int)
    return historical_results

def read_train_test_datasets(v_path):
    
    dataset_train = np.loadtxt(v_path + '/dataset_train.txt', delimiter=';')
    dataset_test = np.loadtxt(v_path + '/dataset_test.txt', delimiter=';')

    return dataset_train, dataset_test


def read_features_datasets(v_path, p_prediction_dataset_name = 'dataset_2026.txt'):

    with open(v_path + '/' + p_prediction_dataset_name) as file:
        v_string = file.read()
    v_string = v_string.replace('array(','')
    v_string = v_string.replace(')','')
    return ast.literal_eval(v_string)
