import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import make_pipeline
from imblearn.pipeline import make_pipeline as make_imb_pipeline

def run_knn_analysis(X_train, y_train, param_grid={}, seed=123, preprocessor=None, scoring=None):
    """
    Perform Hyperparameter Optimization for k-Nearest Neighbors on the given data.
    
    Parameters
    ----------
    X_train : pd.DataFrame
        Training data 
    y_train : pd.Series
        Target values 
    param_grid : dict
        Parameter grid for k-Nearest Neighbors
    preprocessor : ColumnTransformer object
        A callable preprocessor function that transforms the training data.
    scoring : dict or str
        Scoring strategy to evaluate the performance of the cross-validated model.
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the results of the k-Nearest Neighbors analysis.
    """
    results = []

    for k in param_grid["n_neighbors"]:
        knn = KNeighborsClassifier(n_neighbors=k)

        pipe = make_pipeline(preprocessor, knn)
        scores = cross_validate(pipe, X_train, y_train, return_train_score=True, scoring=scoring, cv=20)

        # Store the results for each k
        k_results = {"n_neighbors": k, "kNN model": "without oversampling"}
        for metric in scoring.keys():
            test_metric = f"test_{metric}"
            k_results[f"mean_{metric}"] = np.mean(scores[test_metric])
            k_results[f"std_{metric}"] = np.std(scores[test_metric])

        results.append(k_results)
        
        pipe_imb = make_imb_pipeline(RandomOverSampler(sampling_strategy='minority'), preprocessor, knn)
        scores = cross_validate(pipe_imb, X_train, y_train, return_train_score=True, scoring=scoring, cv=20)

        # Store the results for each k
        k_results = {"n_neighbors": k, "kNN model": "with oversampling"}
        for metric in scoring.keys():
            test_metric = f"test_{metric}"
            k_results[f"mean_{metric}"] = np.mean(scores[test_metric])
            k_results[f"std_{metric}"] = np.std(scores[test_metric])

        results.append(k_results)

    # Convert the results to a pandas DataFrame
    results_df = pd.DataFrame(results)
    return results_df