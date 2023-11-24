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


# # Import the run_knn_analysis function from the src folder
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# from src.run_knn_analysis import run_knn_analysis

# setting seed
np.random.seed(123)

def evaluate_logistic_regression(X_train, y_train, X_test, y_test, numeric_features, categorical_features):
    """
    Process the training data and evaluate the logistic regression model on test data.

    Creates a preprocessing pipeline for numeric and categorical features, 
    fits a logistic regression model using GridSearchCV to find the best hyperparameters, 
    and evaluates the model's performance on the test set. 
    It outputs the  confusion matrix , the classification report for the test data, .

    Parameters:
    - X_train (pd.DataFrame): Training data features.
    - y_train (pd.Series): Training data target variable.
    - X_test (pd.DataFrame): Test data features.
    - y_test (pd.Series): Test data target variable.
    - numeric_features (list): List of column names for numeric features.
    - categorical_features (list): List of column names for categorical features.

    Returns:
    - tuple: A tuple containing the Confusion Matrix and the classification report.
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


    # Output best parameters and scores
    print("Best Parameters: ", gs.best_params_)
    print("Best Score: ", gs.best_score_)
    print("Test Set Score: ", gs.score(X_test, y_test))

    # Generate and display confusion matrix
    cm = confusion_matrix(y_test, gs.predict(X_test))
    cm_df = pd.DataFrame(cm, 
                     index=['True: 0', 'True: 1'], 
                     columns=['Pred: 0', 'Pred: 1'])

    print("Confusion Matrix:")
    print(cm_df)


    # Generate and print classification report
    report_string = classification_report(y_test, gs.predict(X_test), zero_division = 1)
    print('Classification Report for Test Data:\n', report_string)
    rt = classification_report(y_test, gs.predict(X_test), zero_division=1, output_dict=True)
    report_df = pd.DataFrame(rt).transpose()
    print(report_df)

    

    return cm_df, report_df, gs, gs_res



