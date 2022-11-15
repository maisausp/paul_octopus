import numpy as np

def read_datasets(p_path = 'dataset/'):
    
    dataset_train = np.loadtxt(p_path + 'dataset_train.txt', delimiter=';')
    dataset_test = np.loadtxt(p_path + 'dataset_test.txt', delimiter=';')

    X_train = dataset_train[:,:-1]
    y = dataset_train[:,-1]

    return X_train, y, dataset_test