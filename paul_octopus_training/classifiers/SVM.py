from sklearn import svm

def fit(X, y):

    clf = svm.SVC()
    clf.fit(X, y)
    return clf