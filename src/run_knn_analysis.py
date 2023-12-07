import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import make_pipeline
from imblearn.pipeline import make_pipeline as make_imb_pipeline

def run_knn_analysis(X_train, y_train, param_grid={}, seed=123, preprocessor=None, scoring=None):
    """
    Conducts k-Nearest Neighbors (kNN) analysis with optional preprocessing and oversampling,
    performing hyperparameter optimization based on the provided parameter grid. 
    The function evaluates the model with and without oversampling for imbalanced datasets.

    Parameters
    ----------
    X_train : pd.DataFrame
        Training feature dataset.
    y_train : pd.Series
        Training target variable.
    param_grid : dict, optional
        Dictionary containing parameters to be tested in kNN. 
        Example: {'n_neighbors': [3, 5, 7]}. Defaults to empty dict.
    seed : int, optional
        Random seed for reproducibility. Defaults to 123.
    preprocessor : sklearn.compose.ColumnTransformer, optional
        A preprocessor pipeline (e.g., for scaling or encoding). Defaults to None.
    scoring : dict or str, optional
        Scoring strategy to evaluate the performance of the cross-validated model. 
        Example: {'accuracy': 'accuracy', 'f1': 'f1'}. Defaults to None.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the cross-validated performance metrics for each value 
        of 'n_neighbors' in the parameter grid, comparing models with and without oversampling.

    Example
    -------
    >>> X_train = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    >>> y_train = pd.Series([0, 1, 0])
    >>> param_grid = {'n_neighbors': [3, 5]}
    >>> results = run_knn_analysis(X_train, y_train, param_grid)
    >>> print(results)
    """
    results = []

    for k in param_grid.get("n_neighbors", [5]):  # Default value set to [5] if not provided
        knn = KNeighborsClassifier(n_neighbors=k)

        # Without oversampling
        pipe = make_pipeline(preprocessor, knn) if preprocessor else make_pipeline(knn)
        scores = cross_validate(pipe, X_train, y_train, return_train_score=True, scoring=scoring, cv=20)

        # Store the results for each k
        k_results = {"n_neighbors": k, "kNN model": "without oversampling"}
        for metric in (scoring or {}).keys():
            test_metric = f"test_{metric}"
            k_results[f"mean_{metric}"] = np.mean(scores[test_metric])
            k_results[f"std_{metric}"] = np.std(scores[test_metric])

        results.append(k_results)
        
        # With oversampling
        pipe_imb = make_imb_pipeline(RandomOverSampler(sampling_strategy='minority'), preprocessor, knn) if preprocessor else make_imb_pipeline(RandomOverSampler(sampling_strategy='minority'), knn)
        scores = cross_validate(pipe_imb, X_train, y_train, return_train_score=True, scoring=scoring, cv=20)

        # Store the results for each k
        k_results = {"n_neighbors": k, "kNN model": "with oversampling"}
        for metric in (scoring or {}).keys():
            test_metric = f"test_{metric}"
            k_results[f"mean_{metric}"] = np.mean(scores[test_metric])
            k_results[f"std_{metric}"] = np.std(scores[test_metric])

        results.append(k_results)

    # Convert the results to a pandas DataFrame
    results_df = pd.DataFrame(results)
    return results_df
