import altair as alt
import pandas as pd

def create_pairwise_scatter_plot(train_df, numerical_features, color_feature=None):
    """
    Revised function to create a pairwise scatter plot matrix.
    """

    # Check if DataFrame is empty
    if train_df.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if all numerical features are in DataFrame
    missing_features = [f for f in numerical_features if f not in train_df.columns]
    if missing_features:
        raise KeyError(f"Missing features in DataFrame: {missing_features}")

    # Base chart
    base = alt.Chart().mark_point(opacity=0.5, size=10)

    # Adding color encoding if color_feature is provided and exists in DataFrame
    if color_feature and color_feature in train_df.columns:
        base = base.encode(color=alt.Color(f'{color_feature}:N'))

    # Creating pairwise scatter plot
    pairwise_chart = alt.layer(
        *[base.encode(
            x=alt.X(feat, type='quantitative'),
            y=alt.Y(other_feat, type='quantitative')
        ).properties(
            width=150,
            height=150
        ) for feat in numerical_features for other_feat in numerical_features if feat != other_feat]
    ).resolve_scale(
        x='independent', 
        y='independent'
    ).properties(
        title='Figure 4: Pairwise Scatter Plot Matrix'
    )

    return pairwise_chart
