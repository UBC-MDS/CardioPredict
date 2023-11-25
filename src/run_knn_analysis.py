import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline

def run_knn_analysis(X_train, y_train, param_grid={}, preprocessor=None):
    """
    Perfrom Hyperparameter Optimization for k-Nearest Neighbors on the given data.

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

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the results of the k-Nearest Neighbors analysis,
        including columns 'n_neighbors', 'mean_train_score', 'mean_cv_score',
        'std_cv_score', and 'std_train_score'.

    Examples
    --------
    >>> X_train, y_train = np.random.randn(100, 10), np.random.choice([0, 1], 100)
    >>> param_grid = {"n_neighbors": np.arange(1, 10, 2)}
    >>> results = run_knn_analysis(X_train, y_train, param_grid, simple_preprocessor)
    >>> print(results)
    """
    results_dict = {
        "n_neighbors": [],
        "mean_train_score": [],
        "mean_cv_score": [],
        "std_cv_score": [],
        "std_train_score": [],
    }

    for k in param_grid["n_neighbors"]:
        knn = KNeighborsClassifier(n_neighbors=k)
        pipe = make_pipeline(preprocessor, knn)
        scores = cross_validate(pipe, X_train, y_train, return_train_score=True)

        results_dict["n_neighbors"].append(k)
        results_dict["mean_cv_score"].append(np.mean(scores["test_score"]))
        results_dict["mean_train_score"].append(np.mean(scores["train_score"]))
        results_dict["std_cv_score"].append(np.std(scores["test_score"]))
        results_dict["std_train_score"].append(np.std(scores["train_score"]))

    results_df = pd.DataFrame(results_dict)
    return results_df



