import altair as alt
import pandas as pd
import pytest
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
        'feature2': [4, 5, 6],
        'color_feature': ['A', 'B', 'C']
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features, 'color_feature')
    assert isinstance(chart, alt.LayerChart), "The output should be an Altair LayerChart object"

#2. Test for Correct Color Encoding (Optional)
def test_color_encoding():
    # Sample data with color feature
    train_df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'color_feature': ['A', 'B', 'C']
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features, 'color_feature')
    # Checking if color feature is used in any of the layers
    assert any('color_feature:N' in str(layer.encoding.color) for layer in chart.layer), \
        "Color feature should be encoded in at least one layer of the chart"

#3. Test for Absence of Color Encoding
def test_without_color_feature():
    train_df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    assert all('color' not in str(layer.encoding) for layer in chart.layer), \
        "Color encoding should not be set when color_feature is None"

#4. Test for Input Validation
def test_dataframe_input_handling():
    # Empty DataFrame
    train_df_empty = pd.DataFrame()
    numerical_features = ['feature1', 'feature2']
    with pytest.raises(ValueError):
        create_pairwise_scatter_plot(train_df_empty, numerical_features)

    # DataFrame missing specified features
    train_df_missing_features = pd.DataFrame({'feature3': [7, 8, 9]})
    with pytest.raises(KeyError):
        create_pairwise_scatter_plot(train_df_missing_features, numerical_features)
