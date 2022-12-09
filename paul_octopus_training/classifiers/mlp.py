from sklearn.neural_network import MLPClassifier
from joblib import dump, load
import pickle

def fit(X, y):
    
    #clf = MLPClassifier(random_state=1, max_iter=300)
    clf = MLPClassifier(random_state=1, max_iter=300)
    clf.fit(X, y)
    dump(clf, "paul_octopus_training/output/model/MLPClassifier.joblib") 
    
    return clf