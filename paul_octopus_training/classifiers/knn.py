from sklearn.neighbors import KNeighborsClassifier


def fit(X, y):

    knn = KNeighborsClassifier(n_neighbors=1, metric='manhattan')
    knn.fit(X, y)

    return knn
