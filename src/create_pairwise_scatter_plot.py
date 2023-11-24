import altair as alt
import pandas as pd

def create_pairwise_scatter_plot(train_df, numerical_features):
    """
    Creates a pairwise scatter plot matrix from the given DataFrame and numerical features.

    Parameters:
    ----------
    train_df : pandas.DataFrame
        A pandas DataFrame containing the data to be plotted.
    numerical_features : list
        A list of column names in train_df that are numerical features to be included in the scatter plot.

    Returns:
    -------
    alt.Chart
        An Altair Chart object representing the pairwise scatter plot matrix.

    Example:
    --------
    >>> train_df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'disease': ['A', 'B', 'C']
        })
    >>> numerical_features = ['feature1', 'feature2']
    >>> chart = create_pairwise_scatter_plot(train_df, numerical_features)
    >>> chart
    """
    base = alt.Chart(train_df).mark_point(opacity=0.5, size=10)

    pairwise_chart = base.encode(
        x=alt.X(alt.repeat("row"), type='quantitative', scale=alt.Scale(zero=False)),
        y=alt.Y(alt.repeat("column"), type='quantitative', scale=alt.Scale(zero=False)),
        color='disease:N'
    ).properties(
        width=150,
        height=150
    ).repeat(
        row=numerical_features,
        column=numerical_features
    ).resolve_scale(
        x='independent', 
        y='independent'
    )

    pairwise_chart = pairwise_chart.properties(
        title='Figure 4: Pairwise Scatter Plot Matrix'
    )

    return pairwise_chart
