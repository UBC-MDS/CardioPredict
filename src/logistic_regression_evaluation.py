import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report

def evaluate_logistic_regression(X_train, y_train, X_test, y_test, numeric_features, categorical_features):
    """
    Evaluate the logistic regression model with hyperparameter tuning using GridSearchCV.

    Parameters:
    - X_train (pd.DataFrame): Training data features.
    - y_train (pd.Series): Training data target variable.
    - X_test (pd.DataFrame): Test data features.
    - y_test (pd.Series): Test data target variable.
    - numeric_features (list): List of column names for numeric features.
    - categorical_features (list): List of column names for categorical features.

    Returns:
    - results (dict): Dictionary containing the confusion matrix, classification report,
                      fitted GridSearchCV object, and GridSearchCV results.
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
    report = classification_report(y_test, gs.predict(X_test), zero_division=1)

    # Returning results in a dictionary
    results = {
        'confusion_matrix': cm,
        'classification_report': report,
        'grid_search_object': gs,
        'grid_search_results': gs_res
    }

    return results

# Example Usage
'''
# Assuming data is loaded into X_train, y_train, X_test, y_test
# Example of numeric and categorical features
numeric_features = ['age', 'income']
categorical_features = ['gender', 'occupation']

# Call the function
results = evaluate_logistic_regression(X_train, y_train, X_test, y_test, numeric_features, categorical_features)

# Accessing different components of the result
conf_matrix = results['confusion_matrix']
class_report = results['classification_report']
grid_search_cv_object = results['grid_search_object']
grid_search_cv_results = results['grid_search_results']

# Example of how to use these components
print("Confusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)
print("\nBest Parameters from Grid Search:\n", grid_search_cv_object.best_params_)
'''

