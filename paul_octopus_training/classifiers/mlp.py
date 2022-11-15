from sklearn.neural_network import MLPClassifier
from joblib import dump, load

def fit(X, y):
    
    #clf = MLPClassifier(random_state=1, max_iter=300)
    clf = MLPClassifier(random_state=1, max_iter=300)
    clf.fit(X, y)
    dump(clf, "output/model/MLPClassifier.h5") 
    return clf