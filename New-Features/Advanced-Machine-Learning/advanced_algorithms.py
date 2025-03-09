import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class AdvancedMachineLearning:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000)

    def train_model(self, data, labels):
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model trained with accuracy: {accuracy*100:.2f}%")
        return self.model, accuracy

    def evaluate_model(self, model, test_data):
        predictions = model.predict(test_data)
        return predictions
