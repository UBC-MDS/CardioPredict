import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay, classification_report



def evaluate_logistic_regression(X_train, y_train, X_test, y_test, numeric_features, categorical_features):
    """
    Evaluate the logistic regression model with hyperparameter tuning using GridSearchCV.

    This function processes the training data and evaluates the logistic regression model on the test data.
    It creates a preprocessing pipeline for numeric and categorical features and performs hyperparameter 
    tuning to find the best model. It then outputs the confusion matrix and classification report for 
    the test data, along with  the fitted GridSearchCV object and the results of the GridSearchCV.

    Parameters:
    - X_train (pd.DataFrame): Training data features.
    - y_train (pd.Series): Training data target variable.
    - X_test (pd.DataFrame): Test data features.
    - y_test (pd.Series): Test data target variable.
    - numeric_features (list): List of column names for numeric features.
    - categorical_features (list): List of column names for categorical features.

    Returns:
    - cm (numpy.ndarray): Confusion matrix as a 2D numpy array.
    - report (str): Text summary of the precision, recall, F1 score, and support for each class.
    - gs (GridSearchCV): Fitted GridSearchCV object.
    - gs_res (pd.DataFrame): DataFrame containing the cross-validation results from GridSearchCV,
      sorted by the rank of the test score.
    """

    # Create pipeline for numeric features
    numeric_pipe = make_pipeline(
        SimpleImputer(strategy="median"), StandardScaler()
    )

    # Create Column Transformer
    preprocessor = make_column_transformer(
        (numeric_pipe, numeric_features),
        (OneHotEncoder(drop="if_binary", sparse_output=False), categorical_features)
    )

    # Create and fit logistic regression pipeline with grid search
    pipe = make_pipeline(preprocessor, LogisticRegression(class_weight={0: 1, 1: 6}))
    param_grid = {"logisticregression__C": 10.0 ** np.arange(-4, 6, 1)}
    gs = GridSearchCV(pipe, param_grid=param_grid, n_jobs=-1, return_train_score=True)
    gs.fit(X_train, y_train)

    gs_res = pd.DataFrame(gs.cv_results_)[[
    'rank_test_score', 'param_logisticregression__C', 
    'mean_train_score', 'std_train_score', 'mean_test_score', 'std_test_score']].sort_values('rank_test_score')


 

    # Generate the confusion matrix
    cm = confusion_matrix(y_test, gs.predict(X_test))

    # Generate and print classification report
    report = classification_report(y_test, gs.predict(X_test), zero_division = 1)

    return cm, report, gs, gs_res
