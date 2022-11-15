import pandas as pd
import numpy as np
import ast


def read_historical_results():
    
    historical_results = pd.read_csv('datasets/historical-results.csv', parse_dates = ['date'])    
    return historical_results

def read_train_test_datasets(v_path):
    
    dataset_train = np.loadtxt(v_path + '/dataset_train.txt', delimiter=';')
    dataset_test = np.loadtxt(v_path + '/dataset_test.txt', delimiter=';')

    return dataset_train, dataset_test


def read_features_datasets(v_path):

    with open(v_path + '/dataset_2022.txt') as file:
        v_string = file.read()
    v_string = v_string.replace('array(','')
    v_string = v_string.replace(')','')
    return ast.literal_eval(v_string)