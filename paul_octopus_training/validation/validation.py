import numpy as np
import utils.utils as utils

def validate(p_model, test_dataset):

    X_test = test_dataset[:,:-1]
    y_test = test_dataset[:,-1:]
    v_prediction = p_model.predict(X_test)
    #predicted_class = np.argmax(v_prediction, axis=1)

    utils.plot_confusion_matrix(y_test, v_prediction)