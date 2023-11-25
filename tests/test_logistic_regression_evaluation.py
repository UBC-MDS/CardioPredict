import sys
import os
import pytest
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix



# Add the parent directory to the sys.path to allow imports from the src directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# import module
from src.logistic_regression_evaluation import evaluate_logistic_regression


# Test data for 'evaluate_logistic_regression'

# set seed for reproducibility
np.random.seed(123)  
num_samples = 100
test_data_lr = {
    'AGE': np.random.randint(18, 100, num_samples),
    'FRW': np.random.randint(52, 223, num_samples),
    'SBP': np.random.randint(90, 301, num_samples),
    'DBP': np.random.randint(50, 161, num_samples),
    'CHOL': np.random.randint(96, 431, num_samples),
    'CIG': np.random.randint(0, 61, num_samples),
    'sex': np.random.choice(['Female', 'Male'], num_samples),
    'disease': np.random.choice([0, 1], num_samples)
}
df = pd.DataFrame(test_data_lr)
X = df.drop('disease', axis=1)
y = df['disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
numeric_features = ['AGE', 'FRW', 'SBP', 'DBP', 'CHOL', 'CIG']
categorical_features = ['sex']



# Test for correct return type
def test_evaluate_logistic_regression_output_type():
    cm, report, gs, gs_res = evaluate_logistic_regression(
        X_train, y_train, X_test, y_test, numeric_features, categorical_features
    )
    assert isinstance(cm, np.ndarray), "'evaluate_logistic_regression' should return a numpy array for the confusion matrix"
    assert isinstance(report, str), "'evaluate_logistic_regression' should return a string for the classification report"
    assert isinstance(gs, GridSearchCV), "'evaluate_logistic_regression' should return a GridSearchCV object"
    assert isinstance(gs_res, pd.DataFrame), "'evaluate_logistic_regression' should return a pandas DataFrame for the grid search results"


def test_evaluate_logistic_regression_output_format():
    cm, report, gs, gs_res = evaluate_logistic_regression(
        X_train, y_train, X_test, y_test, numeric_features, categorical_features
    )
    
    # Confusion Matrix checks
    assert cm.shape == (2, 2), "Confusion matrix should have a shape of 2x2 for binary classification"
    
    # Classification Report checks
    assert 'precision' in report, "Classification report should contain 'precision'"
    assert 'recall' in report, "Classification report should contain 'recall'"
    assert 'f1-score' in report, "Classification report should contain 'f1-score'"

# Test whether the GridSearchCV is fitted and has the excepted attributes
def test_grid_search_is_fitted():
    cm_df, report_df, gs, gs_res = evaluate_logistic_regression(
        X_train, y_train, X_test, y_test, numeric_features, categorical_features
    )
    # Access the model from the pipeline
    best_model = gs.best_estimator_.named_steps['logisticregression']
    # Check if the model has been fitted
    assert hasattr(best_model, 'coef_'), "The logistic regression model should have fitted coefficients"
    assert hasattr(gs, 'best_estimator_'), "gs should have attribute best_estimator_"
    assert hasattr(gs, 'cv_results_'), "gs should have attribute cv_results_ after fitting"
    assert hasattr(gs, 'best_score_'), "gs should have attribute best_score_ after fitting"
    assert hasattr(gs, 'best_params_'), "gs should have attribute best_params_ after fitting"

# Test whether the results for the grid search are reasonable.
def test_evaluate_logistic_regression_grid_search_results():
    cm_df, report_df, gs, gs_res = evaluate_logistic_regression(
        X_train, y_train, X_test, y_test, numeric_features, categorical_features
    )
    

    # Check for expected columns in the grid search results DataFrame
    expected_columns = [
        'rank_test_score', 'param_logisticregression__C', 
        'mean_train_score', 'std_train_score', 'mean_test_score', 'std_test_score'
    ]
    for col in expected_columns:
        assert col in gs_res.columns, f"Column {col} should be present in the grid search results DataFrame"

    # Check if the DataFrame is sorted by 'rank_test_score' in ascending order
    assert (gs_res['rank_test_score'] == sorted(gs_res['rank_test_score'])).all(), \
        "gs_res should be sorted by 'rank_test_score'"

    # Check that the score columns contain valid score values within [0, 1]
    for col in ['mean_train_score', 'mean_test_score']:
        assert gs_res[col].between(0, 1).all(), f"Scores in column {col} should be between 0 and 1"

    # Check that the standard deviation columns contain non-negative values
    for col in ['std_train_score', 'std_test_score']:
        assert (gs_res[col] >= 0).all(), f"Standard deviations in column {col} should be non-negative"

