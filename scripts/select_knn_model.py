import os
import sys
import click
import pickle
import pandas as pd
import numpy as np
from joblib import load
from sklearn.neighbors import KNeighborsClassifier
from imblearn.pipeline import make_pipeline as make_imb_pipeline
from sklearn.model_selection import cross_validate
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
import altair as alt

import warnings
warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.run_knn_analysis import run_knn_analysis

@click.command()
@click.option('--x_train', type=str, help="Path to X_train")
@click.option('--y_train', type=str, help="Path to y_train")
@click.option('--preprocessor', type=str, help="Path to preprocessor")
@click.option('--seed', type=int, help="Random seed", default=123)
@click.option('--table-results-to', type=str, help="Path to directory where the result table will be written to")
@click.option('--figure-results-to', type=str, help="Path to directory where the result table will be written to")

def main(x_train, y_train, preprocessor, table_results_to, figure_results_to, seed):
    '''Finds the best k for KK, fits the disease classifier to the training data and saves the pipeline object and cv_results.'''
    #import X_train and y_train
    x_train = pd.read_csv(x_train)
    y_train = pd.read_csv(y_train)

    #load the preprocessor
    # Load the preprocessor
    with open(preprocessor, 'rb') as f:
        preprocessor = pickle.load(f)
    #print(f"Loaded Preprocessor: {preprocessor}")  # Debug print

    scoring_metrics = {
        'accuracy': make_scorer(accuracy_score),
        'precision': make_scorer(precision_score, pos_label=1),
        'recall': make_scorer(recall_score, pos_label=1),
        'f1_score': make_scorer(f1_score, pos_label=1)
    }
    
    #Search the best k for knn
    param_grid = {"n_neighbors": np.arange(1, 20, 1)}
    df_cv_knn = run_knn_analysis(x_train, y_train, param_grid, 
                                 preprocessor=preprocessor, scoring=scoring_metrics)


    df_cv_knn.to_csv(os.path.join(table_results_to, "result_knn.csv"), index=False)

    accuracy_chart = alt.Chart(df_cv_knn).mark_line(point=True).encode(
        x=alt.X('n_neighbors:O', title='Neighbors', axis=alt.Axis(labelAngle=0)), 
        y=alt.Y('mean_accuracy:Q', title='Accuracy'),
        color='kNN model:N',
    )

    error_bars_acc = alt.Chart(df_cv_knn).mark_errorbar(extent='ci').encode(
        x=alt.X('n_neighbors:O', title=''), 
        y=alt.Y('mean_accuracy:Q', title=''),
        yError='std_accuracy:Q',
        color='kNN model:N'
    )

    # Create the line chart for recall with error bars
    recall_chart = alt.Chart(df_cv_knn).mark_line(point=True).encode(
        x=alt.X('n_neighbors:O', title='Neighbors', axis=alt.Axis(labelAngle=0)), 
        y=alt.Y('mean_recall:Q', title='Recall'),
        color='kNN model:N',
    )

    error_bars_rec = alt.Chart(df_cv_knn).mark_errorbar(extent='ci').encode(
        x=alt.X('n_neighbors:O', title=''), 
        y=alt.Y('mean_recall:Q', title=''),
        yError='std_recall:Q',
        color='kNN model:N'
    )

    # Combine the charts side by side
    accuracy_chart = accuracy_chart + error_bars_acc
    recall_chart = recall_chart + error_bars_rec

    # Save the chart
    accuracy_chart.save(os.path.join(figure_results_to, "accuracy_lines.png"),
              scale_factor=2.0)
    recall_chart.save(os.path.join(figure_results_to, "recall_lines.png"),
              scale_factor=2.0)
    print('Line plots saved!')

if __name__ == '__main__':
   main()

# python scripts/select_knn_model.py --x_train=data/processed/X_train.csv --y_train=data/processed/y_train.csv --preprocessor=results/models/preprocessor.pickle  --table-results-to=results/tables --figure-results-to=results/figures