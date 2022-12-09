from keras.callbacks import ModelCheckpoint
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

def getCallBacks(vPathFileName = 'output/Checkpoint/'):
    '''
    Função chamada durante o treino para salvar os pesos obtidos na RN.
    '''
    checkpoint = ModelCheckpoint(vPathFileName, monitor='val_accuracy', verbose=0,
                                 save_best_only=True, save_weights_only=True,
                                 mode='auto')
    return [checkpoint]

def plot_history(p_history):
  #ToDo mudar para save  
  '''
  Função que plota o gráfico com a evolução do treino, em relação a valores de erro e acurácia para os datasets de treino e validação.
  '''
  # summarize history for accuracy
  plt.plot(p_history.history['accuracy'])
  plt.plot(p_history.history['val_accuracy'])
  plt.title('model accuracy')
  plt.ylabel('accuracy')  
  plt.xlabel('epoch')
  plt.legend(['train', 'validation'], loc='upper left')
  plt.ylim(0, 1)  
  plt.show()
  plt.savefig("paul_octopus_training/images/history_accuracy.png", format="PNG")
  plt.close()
  
  # summarize history for loss
  plt.plot(p_history.history['loss'])
  plt.plot(p_history.history['val_loss'])
  plt.title('model loss')
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.legend(['train', 'validation'], loc='upper left')
  plt.show()
  plt.savefig("paul_octopus_training/images/history_loss.png", format="PNG")

def plot_confusion_matrix(p_y_real, p_y_predicted):

  print("Accuracy model")
  print(accuracy_score(p_y_real, p_y_predicted))

  cm = confusion_matrix(p_y_real, p_y_predicted)
  disp = ConfusionMatrixDisplay(confusion_matrix=cm)

  disp.plot()
  plt.show()
  plt.savefig("paul_octopus_training/images/confusion_matrix.png", format="PNG")