import altair as alt

def create_pairwise_scatter_plot(df, features):
    """
    Revised function to create a pairwise scatter plot matrix.
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
