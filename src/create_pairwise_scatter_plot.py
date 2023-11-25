import altair as alt

def create_pairwise_scatter_plot(df, features):
    """
    Create a pairwise scatter plot matrix from a given DataFrame and a list of features.

    This function generates a matrix of scatter plots, each plot comparing two different
    features from the provided list. The plots use independent scales for each axis and 
    points are colored by the 'disease' category. Opacity and size of points are set for 
    better visibility. 

    Parameters:
    df (DataFrame): The DataFrame containing the data to plot.
    features (list of str): A list of column names from the DataFrame to be used as features for the scatter plots.

    Returns:
    Chart: An Altair Chart object representing the pairwise scatter plot matrix.
    """
    base = alt.Chart(df).mark_point(opacity=0.5, size=10)

    # Create pairwise scatter plot with independent scales
    pairwise_chart = base.encode(
        x=alt.X(alt.repeat("row"), type='quantitative', scale=alt.Scale(zero=False)),
        y=alt.Y(alt.repeat("column"), type='quantitative', scale=alt.Scale(zero=False)),
        color='disease:N'
    ).properties(
        width=150,
        height=150
    ).repeat(
        row=features,
        column=features
    ).resolve_scale(
        x='independent', 
        y='independent'
    )

    pairwise_chart = pairwise_chart.properties(
        title='Figure 4: Pairwise Scatter Plot Matrix'
    )

    return pairwise_chart
