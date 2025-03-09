from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier

class ModelTuning:
    def __init__(self, model):
        self.model = model

    def tune_model(self, data, labels):
        param_grid = {
            'hidden_layer_sizes': [(50,), (100,), (200,)],
            'max_iter': [100, 200, 500]
        }
        grid_search = GridSearchCV(self.model, param_grid, cv=3, verbose=1)
        grid_search.fit(data, labels)
        best_params = grid_search.best_params_
        print(f"Best parameters: {best_params}")
        return best_params
