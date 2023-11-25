# author: Doris Wang
# date: 2023-11-23

import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(input_file, output_train_file, output_test_file, test_size=0.2, random_state=123):
    """
    Splits a dataset into training and testing sets and saves them as CSV files.

    This function reads a dataset from a CSV file, splits it into training and
    testing sets based on the specified test size and random state, and then 
    saves these sets into separate CSV files.

    Parameters:
    -----------
    input_file : str
        Path to the input CSV file containing the dataset.
    output_train_file : str
        Path where the training set CSV file will be saved.
    output_test_file : str
        Path where the testing set CSV file will be saved.
    test_size : float, optional
        Proportion of the dataset to include in the test split (default is 0.2).
    random_state : int, optional
        Seed for the random number generator (default is 123).

    Returns:
    --------
    tuple of pandas.DataFrame
        A tuple containing two dataframes (train_df, test_df).

    Examples:
    ---------
    >>> train_df, test_df = split_data("data/full_dataset.csv", "data/train_set.csv", "data/test_set.csv", test_size=0.25, random_state=42)
    This will read 'full_dataset.csv', split it into training and testing sets with
    25% of the data as the test set using a random state of 42, and save these sets
    to 'train_set.csv' and 'test_set.csv', respectively.
    """

    # Read data
    df = pd.read_csv(input_file)

    # Split data
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)

    # Save to CSV
    train_df.to_csv(output_train_file, index=False)
    test_df.to_csv(output_test_file, index=False)

    return train_df, test_df
