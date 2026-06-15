import numpy as np

def read_datasets(p_nr_classes, p_path = 'paul-octopus-2026/datasets/all_score/48_or_4_year/'):
    
    dataset_train = np.loadtxt(p_path + 'dataset_train.txt', delimiter=';')
    dataset_test = np.loadtxt(p_path + 'dataset_test.txt', delimiter=';')

    X_train = dataset_train[:,:-1]
    y = dataset_train[:,-1]
    #y_train = np_utils.to_categorical(y, num_classes=p_nr_classes)

    return X_train, y, dataset_test
