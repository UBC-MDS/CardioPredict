import pytest
import sys
import os
import numpy as np
import random
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Import the run_knn_analysis function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.run_knn_analysis import run_knn_analysis

# setting seed
np.random.seed(42)

# Test data for 'run_knn_analysis'
test_data_knn = {
    'Numerical_1': np.random.uniform(-2, 2, 20),
    'Numerical_2': np.random.uniform(-2, 2, 20),
    'Numerical_3': np.random.uniform(-2, 2, 20),
    'Categorical_1': [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)],
    'Categorical_2': [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)]
}

train_x = pd.DataFrame(test_data_knn)
train_y = np.random.choice([0, 1], 20)
numerical_cols = ['Numerical_1', 'Numerical_2', 'Numerical_3']
categorical_cols = ['Categorical_1', 'Categorical_2']

preprocessor = make_column_transformer(
        (StandardScaler(), numerical_cols),  # Standardize numerical columns
        (OneHotEncoder(handle_unknown="ignore"), categorical_cols)   # One-hot encode categorical columns
    )

param_grid = {"n_neighbors": np.arange(1, 10, 2)}


# Test for correct return type 
def test_knn_output_type():
    output_knn = run_knn_analysis(train_x, train_y, param_grid, preprocessor)
    assert isinstance(output_knn, pd.DataFrame), "'run_knn_analysis' should return a pandas data frame"

#Test whether the values for the calculated train- and test scores are reasonable
def test_knn_score_value():
    result = run_knn_analysis(train_x, train_y, param_grid, preprocessor)
    assert all(0 <= score <= 1 for score in result["mean_train_score"]), "Score needs to lie within the range of 0 and 1"
    assert all(0 <= score <= 1 for score in result["mean_cv_score"]), "Score needs to lie within the range of 0 and 1"
    assert all(score >= 0 for score in result["std_cv_score"]), "Standard Deviation needs to be a positive value"
    assert all(score >= 0 for score in result["std_train_score"]), "Standard Deviation needs to be a positive value"

#Test for correct column names in the output table: 
def test_knn_correct_columns():
    expected_columns = ["n_neighbors", "mean_train_score", "mean_cv_score", "std_cv_score", "std_train_score"]
    assert all(col in run_knn_analysis(train_x, train_y, param_grid, preprocessor).columns for col in expected_columns)


#Test whether all the values in the param_grid appear in the data frame
def test_knn_neighbor():
    result_knn = run_knn_analysis(train_x, train_y, param_grid, preprocessor)
    assert all(n in result_knn["n_neighbors"].values for n in param_grid["n_neighbors"])
    assert result_knn.shape[0] == len(param_grid["n_neighbors"]), "Not all neighbors are represented in the data frame"


#Test for correct error handling for missing arguments
def test_knn_missing__error():
    with pytest.raises(TypeError) as custom_string:
        run_knn_analysis(train_y, param_grid=param_grid, preprocessor=preprocessor)
    assert str(custom_string.value), "X_train is required as an additional argument"

    with pytest.raises(TypeError) as custom_string:
        run_knn_analysis(train_x, param_grid=param_grid, preprocessor=preprocessor)
    assert str(custom_string.value), "y_train is required as an additional argument"

    with pytest.raises(KeyError) as custom_string:
        run_knn_analysis(train_x, train_y, preprocessor=preprocessor)
    assert str(custom_string.value), "Parameter grid is required"


#Test for correct error handling for incorrect order of arguments
def test_knn_type__error_order():
    with pytest.raises(TypeError) as custom_string:
        run_knn_analysis(train_y, train_x, param_grid, preprocessor)
    assert str(custom_string.value), "y_train needs to be 1-dimensional array-like object"

    with pytest.raises(TypeError) as custom_string:
        run_knn_analysis(train_x, train_y, preprocessor, param_grid)
    assert str(custom_string.value), "The order of arguments in run_knn_analysis is incorrect. Expected order: X_train, y_train, param_grid, preprocessor."


