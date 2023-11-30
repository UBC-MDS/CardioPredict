import altair as alt
import click
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@click.command()
@click.option('--df', type=str, help="Path to training data")
@click.option('--plot-to', type=str, help="Path to directory where the plot will be written to")
@click.option('--data-to', type=str, help="Path to directory where data.csv will be saved to")

def main(df, plot_to, data_to):
    """
    Plots 5 charts in training data and displays them as a grid of plots. Also saves the plots
    """

    df = pd.read_csv(df)
    # 1.distribution of target feature
    target_chart = alt.Chart(df).mark_bar().encode(
    x='disease:O',
    y=alt.Y('count():Q', axis=alt.Axis(title='Count')),
    text=alt.Text('count():Q')
    ).properties(
    height=200,
    width=200
    )

    target_chart = target_chart + target_chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-5
    )

    target_chart.save(os.path.join(plot_to, "distribution_of_disease_occurrence.png"),
              scale_factor=2.0)

    # 2. Distribution of numerical features
    numerical_features = ['AGE', 'FRW', 'SBP', 'DBP', 'CHOL', 'CIG']

    numerical_chart = alt.Chart(df).transform_calculate(
        disease_label="datum.disease == 1 ? '1: have heart disease' : '0: do not have heart disease'"
    ).mark_bar(opacity=0.8).encode(
        alt.X(alt.repeat('repeat'), type='quantitative', bin=alt.Bin(maxbins=20)),
        alt.Y('count()', stack=None),
        color=alt.Color('disease_label:N', legend=alt.Legend(title="Disease Status"))
    ).properties(
        width=200,
        height=200
    ).repeat(
        repeat=numerical_features, 
        columns=3
    )
    numerical_chart.save(os.path.join(plot_to, "age_and_health_indicators_exhibit_elevated_heart_disease.png"),
              scale_factor=2.0)
    pd.DataFrame(numerical_features, columns=['numerical_features']).to_csv(os.path.join(data_to, "numerical_features.csv"), index=False)

    # 3. correlation matrix
    # Calculate correlation matrix
    correlation_matrix = df.select_dtypes(include=['number', 'bool']).corr('spearman')
    # Create a figure and axis in Matplotlib
    fig, ax = plt.subplots(figsize=(10, 8))
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    # Draw the heatmap using Matplotlib's `imshow` function
    cax = ax.imshow(correlation_matrix, interpolation="nearest", cmap='Blues')
    fig.colorbar(cax)
    # Set ticks
    ax.set_xticks(np.arange(len(correlation_matrix.columns)))
    ax.set_yticks(np.arange(len(correlation_matrix.columns)))
    ax.set_xticklabels(correlation_matrix.columns)
    ax.set_yticklabels(correlation_matrix.columns)
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    # Loop over data dimensions and create text annotations
    for i in range(len(correlation_matrix.columns)):
        for j in range(len(correlation_matrix.columns)):
            if not mask[i, j]:
                text = ax.text(j, i, round(correlation_matrix.iloc[i, j], 2),
                            ha="center", va="center", color="black")

    plt.savefig(os.path.join(plot_to, "correlation_matrix_of_the_features.png"), dpi=300)

    # 4. Create pairwise scatter plot with independent scales
    base = alt.Chart(df).mark_point(opacity=0.5, size=10)
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

    pairwise_chart.save(os.path.join(plot_to, "pairwise_scatter_plot_matrix.png"),
              scale_factor=2.0)

    #5. Distribution of the variable sex
    sex_chart = alt.Chart(df).mark_bar().encode(
        y="sex",
        x= "count()",
        color = "disease:N"
    )
    sex_chart.save(os.path.join(plot_to, "distribution_of_the_sex_variable.png"),
              scale_factor=2.0)

if __name__ == '__main__':
    main()
