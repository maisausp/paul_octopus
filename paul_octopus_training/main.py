import training.training as trainer
import validation.validation as validator
import read.read as reader
import sklearn.utils as sk_utils
import numpy as np
from joblib import dump, load
import classifiers.knn as knn_classifier
import classifiers.SVM as svm_classifier
import classifiers.randomforest as randomForest_classifier
import classifiers.naivebayes as naivebayes_classifier
import classifiers.mlp as mlp_classifier
import classifiers.logistic_regression as logistic_regression_classifier
import classifiers.linear_svm as linear_svm
import classifiers.lda as lda

C_NR_GOLS = 8
C_NR_CLASSES = C_NR_GOLS + 1

def get_training_params():
    params = dict()
    params['input_size'] = 10
    params['nr_classes'] = C_NR_CLASSES
    params['learning_rate'] = 0.0001
    params['num_dense_layers'] = 1
    params['num_dense_nodes'] = 3 #24
    params['activation'] = 'relu'
    params['class_weight'] = {0: 1, 1: 1, 2: 1, 3: 1, 4:1, 5:1, 6:1, 7:1, 8:1}
    #params['class_weight'] = {0: 1.30, 1: 1, 2: 1.8, 3: 2, 4:1, 5:1, 6:1, 7:1, 8:1} #-> 0.328125, mc boa
    #params['class_weight'] = {0: 1, 1: 1, 2: 1, 3: 1, 4:1, 5:1, 6:1, 7:1, 8:1} 

    return params

def get_weights(y):
    
    y_class = np.argmax(y, axis=1)
    weights = sk_utils.compute_class_weight(class_weight = 'balanced', classes = np.unique(y_class), y = y_class)
    class_weight = {0: weights[0], 1: weights[1], 2: weights[2], 3: weights[3], 4: weights[4], 5: weights[5], 6: weights[6], 7: weights[7], 8: weights[8]}
    #class_weight = {0: weights[0], 1: weights[1], 2: weights[2], 3: weights[3], 4: weights[4]}
    #class_weight = {0: weights[0], 1: weights[1], 2: weights[2], 3: weights[3]}
    #class_weight = {0: weights[0], 1: weights[1], 2: weights[2]}
    
    return class_weight

if __name__ == '__main__':

    
    X_train, y_train, dataset_test = reader.read_datasets(C_NR_CLASSES)
    v_model = knn_classifier.fit(X_train, y_train)
    #v_model = svm_classifier.fit(X_train, y_train)
    #v_model = randomForest_classifier.fit(X_train, y_train)
    #v_model = naivebayes_classifier.fit(X_train, y_train)
    #v_model = mlp_classifier.fit(X_train, y_train)
    #v_model = logistic_regression_classifier.fit(X_train, y_train)
    #v_model = linear_svm.fit(X_train, y_train)
    #v_model = lda.fit(X_train, y_train)

    #v_params = get_training_params()    
    #v_params['class_weight'] = get_weights(y_train)

    #v_model = trainer.training(X_train, y_train, v_params) # Novo modelo
    #v_model = trainer.training_continue(X_train, y_train, v_params['class_weight'])
    
    #v_th_score = 3
    #validator.validate(v_model, dataset_test[dataset_test[:, -1] < v_th_score])
    #v_model = load("output/model/MLPClassifier.h5")
    validator.validate(v_model, dataset_test)
    print("Terminou")