class Predictor:
    def __init__(self, model_path):
        import joblib
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        import numpy as np
        input_array = np.array(input_data).reshape(1, -1)
        prediction = self.model.predict(input_array)
        return prediction[0]