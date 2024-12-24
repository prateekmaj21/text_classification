import time
from functools import wraps

def monitor_prediction_time():
    """
    Decorator to monitor the time taken for a prediction.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            prediction_time = end_time - start_time
            print(f"Prediction took {prediction_time:.4f} seconds")
            return result
        return wrapper
    return decorator
