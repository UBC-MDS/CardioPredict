
import altair as alt
import pandas as pd
import sys
import os

# Import the function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_pairwise_scatter_plot import create_pairwise_scatter_plot

# Sample DataFrame and features
train_df = pd.DataFrame({
    'feature1': [1, 2, 3],
    'feature2': [4, 5, 6],
    'disease': ['A', 'B', 'C']
})
numerical_features = ['feature1', 'feature2']

def test_chart_structure():
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    assert isinstance(chart, alt.Chart), "The chart should be an instance of alt.Chart"
    assert chart.title == 'Figure 4: Pairwise Scatter Plot Matrix', "Chart title is incorrect"

def test_marks():
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    assert all(mark.type == 'point' for mark in chart.layer), "All marks should be of type 'point'"
    assert all(mark.opacity == 0.5 and mark.size == 10 for mark in chart.layer), "Marks should have the specified opacity and size"

def test_encoding():
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    for layer in chart.layer:
        assert layer.encoding.x.shorthand.endswith(':Q'), "X-axis should be quantitative"
        assert layer.encoding.y.shorthand.endswith(':Q'), "Y-axis should be quantitative"
        assert layer.encoding.color.shorthand == 'disease:N', "Color encoding should be based on 'disease'"

def test_layout():
    chart = create_pairwise_scatter_plot(train_df, numerical_features)
    for layer in chart.layer:
        assert layer.width == 150 and layer.height == 150, "Subplots should have the specified width and height"

    assert set(chart.repeat.row) == set(numerical_features), "Rows should be based on numerical features"
    assert set(chart.repeat.column) == set(numerical_features), "Columns should be based on numerical features"
