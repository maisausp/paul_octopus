from sklearn.linear_model import LogisticRegression

def fit(X, y):
    clf = LogisticRegression(random_state=0)
    clf.fit(X, y)
    return clf