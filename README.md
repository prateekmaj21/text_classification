# SVM Text Classification API

This project provides a FastAPI-based API for text classification using an SVM model. The API allows users to send text for classification and receive predictions along with their probabilities.

## Project Directory Structure

| Folder/File            | Description             |
|------------------------|-------------------------|
| `text_classification/`  | Root directory          |
| `app/`                  | Contains FastAPI app    |
| `app/main.py`           | FastAPI app             |
| `app/routes.py`         | API routes              |
| `model/`                | Contains model files    |
| `model/train.py`        | Model training          |
| `model/predict.py`      | Prediction logic        |
| `requirements.txt`      | Dependencies            |
| `README.md`             | Documentation           |


## Installation

### 1. Install Dependencies

To get started, clone the repository and install the required dependencies.

```bash
pip install -r requirements.txt
```

### 2.  Train the Model

Before running the FastAPI server, you need to train the model. Use the following command to train the SVM model:

```bash
python model/train.py
```

This will load the image dataset, extract features, train the SVM model, and save it as `svm_image_model.pkl` in the `model/ directory`.

### 3. Run FastAPI Server

Once the model is trained, you can run the FastAPI server with the following command:

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`

