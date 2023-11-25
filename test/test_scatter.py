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
        'feature2': [4, 5, 6]
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    assert isinstance(chart, alt.RepeatChart), "The output should be an Altair RepeatChart object"

#2 Test for Correct Encoding of Features:
def test_feature_encoding():
    train_df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9]
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features)

    encoded_features = set()
    for enc in chart.spec.spec.encoding:
        if enc in ['x', 'y']:
            encoded_features.add(str(chart.spec.spec.encoding[enc].field))

    assert encoded_features == {'feature1', 'feature2'}, \
        "All specified features should be correctly encoded in the chart"

#3.Test for Handling of Non-Numerical Features:
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

#4.Test for Correct Chart Properties
def test_chart_properties():
    train_df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    })
    numerical_features = ['feature1', 'feature2']
    chart = create_pairwise_scatter_plot(train_df, numerical_features)

    assert chart.properties['title'] == 'Figure 4: Pairwise Scatter Plot Matrix', "Chart should have the correct title"
    for subchart in chart.spec:
        assert subchart.properties['width'] == 150, "Subcharts should have the correct width"
        assert subchart.properties['height'] == 150, "Subcharts should have the correct height"
