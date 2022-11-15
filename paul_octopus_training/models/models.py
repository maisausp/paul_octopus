from keras.layers import Dense, Dropout, InputLayer
from keras.models import Sequential
import keras as keras

def get_model(p_input_size, p_nr_classes, learning_rate, num_dense_layers, num_dense_nodes, activation):
    '''
    Função que cria o modelo de RN conforme parametros fornecidos.
    '''

    model = Sequential()
    model.add(InputLayer(input_shape=(p_input_size)))
    model.add(Dense(48, activation='relu', kernel_initializer='random_normal')) 
    model.add(Dense(48, activation='relu', kernel_initializer='random_normal')) 
    model.add(Dense(48, activation='relu', kernel_initializer='random_normal')) 
    model.add(Dense(12, activation='relu', kernel_initializer='random_normal')) 
    model.add(Dense(12, activation='relu', kernel_initializer='random_normal')) 
    model.add(Dense(12, activation='relu', kernel_initializer='random_normal')) 
    model.add(Dense(3, activation='relu', kernel_initializer='random_normal'))
    model.add(Dense(3, activation='relu', kernel_initializer='random_normal'))
    model.add(Dense(3, activation='relu', kernel_initializer='random_normal'))
    #model.add(Dense(num_dense_nodes, activation=activation, kernel_initializer='random_normal')) 
    
    #for i in range(num_dense_layers):
    #model.add(Dropout(0.25))   
    
    model.add(Dense(p_nr_classes, activation='softmax', kernel_initializer='random_normal'))	      
    
    v_optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(loss='categorical_crossentropy', optimizer=v_optimizer, metrics=['accuracy'])
    return model