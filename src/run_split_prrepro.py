# author: Doris Wang
# date: 2023-11-23

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_and_split_data(input_file, output_train_file, output_test_file, numeric_features, categorical_features, test_size=0.2, random_state=123):
    """
    Reads data, preprocesses, splits into train and test sets, and writes them to CSV files.

    Parameters:
    ----------
    input_file : str
        Path to the input CSV file.
    output_train_file : str
        Path to the output CSV file for the training data.
    output_test_file : str
        Path to the output CSV file for the testing data.
    numeric_features : list
        List of numeric feature names for scaling.
    categorical_features : list
        List of categorical feature names for one-hot encoding.
    test_size : float, optional
        Proportion of the dataset to include in the test split (default 0.2).
    random_state : int, optional
        Seed for the random number generator (default 123).

    Returns:
    -------
    None

    Examples:
    --------
    To use this function, provide the paths to your input data and output files,
    along with the lists of numeric and categorical features:

    >>> preprocess_and_split_data("path/to/framingham.csv", 
                                  "path/to/train_df.csv", 
                                  "path/to/test_df.csv",
                                  ['AGE', 'FRW', 'SBP', 'DBP', 'CHOL', 'CIG'], 
                                  ['sex'])
    
    This will read the 'framingham.csv' file, perform preprocessing, split the data into
    training and testing sets, and then save these sets to 'train_df.csv' and 'test_df.csv'.
    """
    # Read data
    df = pd.read_csv(input_file)

    # Split data
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)

    # Preprocess training data
    preprocessor = make_column_transformer(
        (Pipeline([('scaler', StandardScaler())]), numeric_features),
        (OneHotEncoder(drop="if_binary", sparse_output=False), categorical_features)
    )
    train_df_processed = pd.DataFrame(
        preprocessor.fit_transform(train_df),
        columns=numeric_features + list(preprocessor.named_transformers_['onehotencoder'].get_feature_names_out())
    )

    # Save processed training data and unprocessed testing data to CSV
    train_df_processed.to_csv(output_train_file, index=False)
    test_df.to_csv(output_test_file, index=False)


