import altair as alt
import pandas as pd
import pytest
import sys
import os

# Import the function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_pairwise_scatter_plot import create_pairwise_scatter_plot

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'disease': ['A', 'B', 'C']
    }), ['feature1', 'feature2']

def test_chart_structure(sample_data):
    df, features = sample_data
    chart = create_pairwise_scatter_plot(df, features)
    assert isinstance(chart, alt.Chart), "The function should return an instance of alt.Chart"

def test_marks(sample_data):
    df, features = sample_data
    chart = create_pairwise_scatter_plot(df, features)
    for mark in chart.mark:
        assert mark.type == 'point', "All marks should be points"

def test_encoding(sample_data):
    df, features = sample_data
    chart = create_pairwise_scatter_plot(df, features)
    # Check for correct encoding of axes and color
    assert 'x' in chart.encoding and 'y' in chart.encoding, "Chart should have x and y encoding"
    assert 'color' in chart.encoding, "Chart should have color encoding"

def test_layout(sample_data):
    df, features = sample_data
    chart = create_pairwise_scatter_plot(df, features)
    assert chart.width == 150 and chart.height == 150, "Each subplot should have the specified width and height"

def test_error_handling():
    with pytest.raises(ValueError):
        create_pairwise_scatter_plot(None, ['feature1', 'feature2'])
    with pytest.raises(ValueError):
        create_pairwise_scatter_plot(sample_data()[0], ['non_existent_feature'])
