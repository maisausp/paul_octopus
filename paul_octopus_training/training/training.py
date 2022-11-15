import utils.utils as utils
import models.models as models
from keras.models import load_model

def training(X, y, p_params):

    
    model = models.get_model(p_params['input_size'], p_params['nr_classes'], p_params['learning_rate'], p_params['num_dense_layers'], p_params['num_dense_nodes'], p_params['activation'])

    history = model.fit(x=X, y=y, epochs=10000, batch_size=int(X.shape[0]/4), validation_split=0.2,
                        callbacks=utils.getCallBacks(), class_weight=p_params['class_weight'])

    utils.plot_history(history)
    model.save("output/model/model.h5")
    return model

def training_continue(X, y, p_class_weight):
    #0.415929
    model = load_model('output/model/model.h5')
    history = model.fit(x=X, y=y, epochs=100000, batch_size=int(X.shape[0]/4), validation_split=0.2,
                        callbacks=utils.getCallBacks(), class_weight=p_class_weight)

    utils.plot_history(history)
    model.save("output/model/model.h5")
    return model