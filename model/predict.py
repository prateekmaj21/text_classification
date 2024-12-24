import joblib
import numpy as np

class ModelPredictor:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, text: str):
        prediction = self.model.predict([text])[0]
        probability = self.model.predict_proba([text])[0]
        
        # Convert numpy.int64 to int
        prediction = int(prediction)
        
        # Convert numpy arrays to lists (if necessary)
        probability = probability.tolist()
        
        return {"prediction": prediction, "probability": probability}
