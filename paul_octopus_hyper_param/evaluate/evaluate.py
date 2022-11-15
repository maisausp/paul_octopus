
from skopt.utils import use_named_args
import models.models as models
from keras.callbacks import TensorBoard
import read.read as reader
from keras import backend as K
import constants.params as global_params
from skopt.space import Real, Categorical, Integer
import sklearn.utils as sk_utils
import numpy as np
from keras.utils import np_utils

# dimensions
dim_class_0_weight = Real(low=0.9, high=1.1, prior='log-uniform', name='class_0_weight')
dim_class_1_weight = Real(low=0.9, high=1.1, prior='log-uniform', name='class_1_weight')
dim_class_2_weight = Real(low=1, high=10, prior='log-uniform', name='class_2_weight')
dim_class_3_weight = Real(low=2, high=3, prior='log-uniform', name='class_3_weight')
dim_class_4_weight = Real(low=9, high=10, prior='log-uniform', name='class_4_weight')

global dimensions_weight
dimensions_weight = [dim_class_0_weight, dim_class_1_weight, dim_class_2_weight, dim_class_3_weight, dim_class_4_weight]

dim_learning_rate = Real(low=0.0000000001, high=10, prior='log-uniform', name='learning_rate')
dim_num_dense_layers = Integer(low=1, high=100, name='num_dense_layers')
dim_num_dense_nodes = Integer(low=1, high=1000, name='num_dense_nodes')
dim_activation = Categorical(categories=['relu', 'sigmoid'], name='activation')#, 'sigmoid'

global dimensions_network
dimensions_network = [dim_learning_rate, dim_num_dense_layers, dim_num_dense_nodes, dim_activation]

@use_named_args(dimensions=dimensions_weight)
def fitness_class_weight(class_0_weight, class_1_weight, class_2_weight, class_3_weight, class_4_weight):
    
    v_nr_classes = global_params.C_NR_CLASSES
    v_nr_features = global_params.C_NR_FEATURES

    model = models.get_model(v_nr_features, v_nr_classes, 0.00020587286566067464, 15, 424, 'relu')

    callback_log = TensorBoard(log_dir="output/callback/", histogram_freq=0, write_graph=True, write_grads=False, write_images=False)    
    class_weight = {0: class_0_weight, 1: class_1_weight, 2: class_2_weight, 3: class_3_weight, 4: class_4_weight}
    
    X, y, _ = reader.read_datasets()    
    y_categorical = np_utils.to_categorical(y, num_classes=v_nr_classes)

    history = model.fit(x=X, y=y_categorical, epochs=200,
                        batch_size=90,
                        validation_split=0.2,
                        callbacks=[callback_log], class_weight=class_weight)

    accuracy_train = history.history['accuracy'][-1]
    accuracy_val = history.history['val_accuracy'][-1]
    
    accuracy = accuracy_train #+ accuracy_val

    print("Accuracy: {0:.2%}".format(accuracy))
    print("Best Accuracy: {0:.2%}".format(global_params.best_accuracy))
    print()

    if accuracy > global_params.best_accuracy:
        model.save("output/model/best_model_train.h5")
        global_params.best_accuracy = accuracy

    del model    
    K.clear_session()    
    return -accuracy # O processo de avaliação dos melhores é de minimização.

@use_named_args(dimensions=dimensions_network)
def fitness_network(learning_rate, num_dense_layers, num_dense_nodes, activation):
    
    v_nr_classes = global_params.C_NR_CLASSES
    v_nr_features = global_params.C_NR_FEATURES

    #(-1.30078125, [0.00020587286566067464, 15, 424, 'relu'])
    model = models.get_model(v_nr_features, v_nr_classes, learning_rate, num_dense_layers, num_dense_nodes, activation)

    callback_log = TensorBoard(log_dir="output/callback/", histogram_freq=0, write_graph=True, write_grads=False, write_images=False)
    
    X, y, _ = reader.read_datasets()
    y_categorical = np_utils.to_categorical(y, num_classes=v_nr_classes)
        
    weights = sk_utils.compute_class_weight(class_weight = 'balanced', classes = np.unique(y), y = y)
    class_weight = {0: weights[0], 1: weights[1], 2: weights[2], 3: weights[3], 4: weights[4], 5: weights[5], 6: weights[6], 7: weights[7], 8: weights[8]}
    #class_weight = {0: weights[0], 1: weights[1], 2: weights[2]}
    history = model.fit(x=X, y=y_categorical, epochs=1000, batch_size=int(X.shape[0]/10), validation_split=0.2, callbacks=[callback_log])#, class_weight=class_weight)

    accuracy_train = history.history['accuracy'][-1]
    accuracy_val = history.history['val_accuracy'][-1]
    
    accuracy = accuracy_train #accuracy_val #+ accuracy_train

    print("Accuracy: {0:.2%}".format(accuracy))
    print("Best Accuracy: {0:.2%}".format(global_params.best_accuracy))
    print()

    if accuracy > global_params.best_accuracy:
        model.save("output/model/best_model_train.h5")
        global_params.best_accuracy = accuracy

    del model    
    K.clear_session()    
    return -accuracy # O processo de avaliação dos melhores é de minimização.