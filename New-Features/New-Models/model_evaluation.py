from sklearn.metrics import accuracy_score

class ModelEvaluation:
    def __init__(self):
        pass

    def evaluate(self, model, X_test, y_test):
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy
