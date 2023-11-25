import altair as alt
import pandas as pd
import pytest
import numpy as np
import sys
import os

# Import the function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_pairwise_scatter_plot import create_pairwise_scatter_plot

#1. Test for Output Chart Type
def test_create_pairwise_scatter_plot():
    # Sample data
    train_df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    assert isinstance(chart, alt.RepeatChart), "The output should be an Altair RepeatChart object"

#2.Test for Handling of Non-Numerical Features:
def test_handling_non_numerical_features():
    train_df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': ['A', 'B', 'C']  # Non-numerical feature
    })
    numerical_features = ['feature1', 'feature2']
    try:
        chart = create_pairwise_scatter_plot(train_df, numerical_features)
        assert True, "Function should handle non-numerical features gracefully"
    except Exception as e:
        assert False, f"Function should not raise an exception for non-numerical features: {e}"

#3Test for Handling of Large Datasets
def test_handling_large_datasets():
    large_df = pd.DataFrame(np.random.rand(1000, 2), columns=['feature1', 'feature2'])
    numerical_features = ['feature1', 'feature2']
    try:
        chart = create_pairwise_scatter_plot(large_df, numerical_features)
        assert True, "Function should handle large datasets without error"
    except Exception as e:
        assert False, f"Function should not raise an exception for large datasets: {e}"

