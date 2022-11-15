from sklearn.naive_bayes import GaussianNB

def fit(X, y):
    gnb = GaussianNB()
    gnb.fit(X, y)
    return gnb