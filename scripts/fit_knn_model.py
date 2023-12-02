import click
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from imblearn.pipeline import make_pipeline as make_imb_pipeline
from joblib import load
import os
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.run_knn_analysis import run_knn_analysis
from sklearn.model_selection import cross_validate

@click.command()
@click.option('--X_train', type=str, help="Path to X_train")
@click.option('--y_train', type=str, help="Path to y_train")
@click.option('--preprocessor', type=str, help="Path to preprocessor")
@click.option('--scoring', type=str, help="Path to scoring function", default=None)
@click.option('--pipeline-to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)
@click.option('--results-to', type=str, help="Path to directory where the result table will be written to")

def main(X_train, y_train, preprocessor, scoring, seed, pipeline_to, results_to):
    '''Finds the best k for KK, fits the disease classifier to the training data and saves the pipeline object and cv_results.'''

    #import X_train and y_train
    X_train = pd.read_csv(X_train)
    y_train = pd.read_csv(y_train)

    #load the preprocessor
    preprocessor = load(preprocessor)

    #Search the best k for knn
    param_grid = {"n_neighbors": np.arange(5, 50, 5)}
    df_cv_knn = run_knn_analysis(X_train, y_train, param_grid, 
                                 preprocessor, scoring, seed).sort_values("mean_cv_score", ascending = False)
    result_knn = df_cv_knn[["n_neighbors", "mean_cv_score"]].head(1)
    best_k = df_cv_knn.iloc[0,0]

    #Create a pipeline with the best k 
    pipe_knn = make_imb_pipeline(RandomOverSampler(random_state=seed),preprocessor, KNeighborsClassifier(n_neighbors=best_k))

    #Report and Save the recall score on validation set together with mean_cv_score
    recall_median = pd.DataFrame(cross_validate(pipe_knn, X_train, y_train, scoring = "recall"))["test_score"].median()
    result_knn['recall_cv_score'] = recall_median
    result_knn.to_csv(os.path.join(results_to, "result_knn.csv"), index=False)
   
    #Fit and save the pipeline 
    pipe_knn_fit = pipe_knn.fit(X_train, y_train) 
    with open(os.path.join(pipeline_to, "pipe_knn.pickle"), 'wb') as f:
        pickle.dump(pipe_knn_fit, f)

if __name__ == '__main__':
   main()

