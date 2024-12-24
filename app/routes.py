from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model.predict import ModelPredictor
from model.monitor import monitor_prediction_time

router = APIRouter()
predictor = ModelPredictor("model/svm_model.pkl")
monitor = monitor_prediction_time()

# Define the request body model
class PredictRequest(BaseModel):
    text: str

@router.post("/predict/")
@monitor
def predict(request: PredictRequest):
    try:
        result = predictor.predict(request.text)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
