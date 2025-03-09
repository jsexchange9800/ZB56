from sklearn.ensemble import RandomForestClassifier

class NewModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train_model(self, data, labels):
        self.model.fit(data, labels)
        return self.model

    def predict(self, model, test_data):
        return model.predict(test_data)
