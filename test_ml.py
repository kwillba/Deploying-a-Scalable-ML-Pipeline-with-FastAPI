import pytest
# TODO: add necessary import
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from ml.model import train_model, compute_model_metrics, inference
from ml.data import process_data


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Verify return from train_model is an expected model type, Random Forest Classifier
    """
    X_train = [[0,1], [1,0], [1,1]]
    y_train = [0,1,1]
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), 'Model Mismatch'


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Verify if compute_model_metrics function returns expected values for metrics
    """
    y_true = np.array([0, 1, 0, 1])
    y_pred = np.array([0, 1, 1, 0,])
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    assert all(isinstance (metric, float) for metric in [precision, recall, f1]), 'Metrics should be floats'
    assert precision == 0.5, f'Precision should be 0.5, got {precision}'
    assert recall == 0.5, f'Recall shyoud be 0.5, got {recall}'
    assert f1 == 0.5, f'F1 shyoud be 0.5, got {f1}'
    


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    verify process_data properly transforms dataset in to numeric without losing features
    """
    raw_data = pd.DataFrame({
        'feature1': ['A', 'B', 'A'],
        'feature2': [1, 2, 3],
        'target': [0,1,1]
    })
    X, y, encoder, lb = process_data(raw_data, categorical_features=['feature1'], label='target')
    assert X.shape[1] > 0, 'Processed data shoud have features'
    assert y.dtype == int, 'Labels should be integers'
    
