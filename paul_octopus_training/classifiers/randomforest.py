from sklearn.ensemble import RandomForestClassifier

def fit(X, y):
    classifier_rf = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=120, n_estimators=1200, oob_score=True)
    classifier_rf.fit(X, y)

    return classifier_rf