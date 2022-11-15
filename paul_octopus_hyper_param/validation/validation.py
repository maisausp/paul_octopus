import numpy as np
from keras.models import load_model
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from matplotlib import pyplot as plt
import constants.params as global_params
import read.read as reader

def plot_confusion_matrix(p_y_real, p_y_predicted):

  print("Accuracy model")
  print(accuracy_score(p_y_real, p_y_predicted))

  cm = confusion_matrix(p_y_real, p_y_predicted)
  disp = ConfusionMatrixDisplay(confusion_matrix=cm)

  disp.plot()
  plt.show()
  plt.savefig("images/confusion_matrix.png", format="PNG")

def validate():

    _, _, test_dataset = reader.read_datasets()

    v_model = load_model('output/model/best_model_train.h5')
    X_test = test_dataset[:,:-1]
    y_test = test_dataset[:,-1:]
    v_prediction = v_model.predict(X_test)
    predicted_class = np.argmax(v_prediction, axis=1)

    plot_confusion_matrix(y_test, predicted_class)