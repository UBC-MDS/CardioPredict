import os
import sys
import click
import pickle
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from imblearn.pipeline import make_pipeline as make_imb_pipeline
from imblearn.over_sampling import RandomOverSampler
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
from math import pi

@click.command()
@click.option('--x_train', type=str, help="Path to X_train")
@click.option('--y_train', type=str, help="Path to y_train")
@click.option('--preprocessor', type=str, help="Path to preprocessor")
@click.option('--pipeline-to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--figure-results-to', type=str, help="Path to directory where the result figure will be written to")

def main(x_train, y_train, preprocessor, pipeline_to, figure_results_to):
    # Import data
    x_train = pd.read_csv(x_train)
    y_train = pd.read_csv(y_train).squeeze()

    # Load the preprocessor
    with open(preprocessor, 'rb') as f:
        preprocessor = pickle.load(f)

    # Instantiate and fit the kNN model
    knn = KNeighborsClassifier(n_neighbors=9)
    pipe_imb = make_imb_pipeline(RandomOverSampler(sampling_strategy='minority'), preprocessor, knn)
    pipe_imb_fit = pipe_imb.fit(x_train, y_train)

    with open(os.path.join(pipeline_to, "imb_knn_pipeline.pickle"), 'wb') as f:
        pickle.dump(pipe_imb_fit, f)

    # Compute permutation importances
    perm_importance = permutation_importance(pipe_imb, x_train, y_train, n_repeats=30, random_state=123)

    # Create DataFrame for feature importances
    importances_df = pd.DataFrame({
        'Feature': [name.split('__')[-1] for name in preprocessor.get_feature_names_out()],
        'Importance': perm_importance.importances_mean
    })

    # Normalize the feature importances for the radar chart
    importances_df['Importance'] /= importances_df['Importance'].max()

    # Number of variables
    categories = list(importances_df['Feature'])
    N = len(categories)

    # We need to repeat the first value to close the circular graph:
    values = importances_df['Importance'].values.flatten().tolist()
    values += values[:1]
    categories += categories[:1]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels
    plt.xticks(angles, categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.5", "0.75"], color="grey", size=7)
    plt.ylim(0, 1)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    # Save figure
    plt.savefig(os.path.join(figure_results_to, "radar_feature_importance.png"), bbox_inches='tight')

    print('Radar plot saved!')

if __name__ == '__main__':
   main()

# python scripts/fit_knn_model.py --x_train=data/processed/X_train.csv --y_train=data/processed/y_train.csv --preprocessor=results/models/preprocessor.pickle  --pipeline-to=results/models --figure-results-to=results/figures