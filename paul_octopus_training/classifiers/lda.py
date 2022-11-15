from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def fit(X, y):
    clf = LinearDiscriminantAnalysis()
    clf.fit(X, y)
    return clf