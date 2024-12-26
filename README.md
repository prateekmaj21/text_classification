# SVM Text Classification API

This project provides a FastAPI-based API for text classification using an SVM model. The API allows users to send text for classification and receive predictions along with their probabilities.

## Data:

# Text Document Classification Dataset

This dataset is designed for text document classification and clustering tasks. It contains 2,225 text samples categorized into five distinct topics: Politics, Sport, Technology, Entertainment, and Business.

## Dataset Overview

- **Number of Rows**: 2,225
- **Number of Columns**: 2
  - `text`: Contains text data from different categories.
  - `label`: Contains numerical labels corresponding to the categories.

### Categories and Labels
| Category       | Label |
|----------------|-------|
| Politics       | 0     |
| Sport          | 1     |
| Technology     | 2     |
| Entertainment  | 3     |
| Business       | 4     |

## Applications

This dataset can be used for:
- **Text Classification**: Assigning a category label to a given text.
- **Document Clustering**: Grouping similar text documents into clusters.

## Dataset Structure

The dataset contains:
1. **Text**: The content of the document.
2. **Label**: The category assigned to the document as a numerical value.

## Example

| Text                             | Label |
|----------------------------------|-------|
| "The government passed a new law"| 0     |
| "The team won the championship"  | 1     |

## Usage

You can use this dataset for:
- Training and evaluating machine learning models for text classification.
- Exploratory data analysis and visualization of text data.
- Clustering tasks to discover hidden structures in text data.

## Source

The dataset is available on Kaggle: [Text Document Classification Dataset](https://www.kaggle.com/datasets/sunilthite/text-document-classification-dataset)




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

