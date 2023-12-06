# author: Doris Wang
# date: 2023-11-24

import pytest
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.run_split import split_data

# Paths for the test data and output files
TEST_INPUT_FILE = "data/toy/test_framingham.csv"
TEST_OUTPUT_TRAIN_FILE = "data/toy/test_train_df.csv"
TEST_OUTPUT_TEST_FILE = "data/toy/test_test_df.csv"

def test_split_data():
    """
    Test the split_data function to ensure it correctly splits the data and creates output files.
    """
    # Ensure the output directories exist
    for file_path in [TEST_OUTPUT_TRAIN_FILE, TEST_OUTPUT_TEST_FILE]:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Test the split_data function
    split_data(TEST_INPUT_FILE, TEST_OUTPUT_TRAIN_FILE, TEST_OUTPUT_TEST_FILE, test_size=0.2, random_state=123)

    # Check if the output files are created
    assert os.path.exists(TEST_OUTPUT_TRAIN_FILE), "Training file was not created."
    assert os.path.exists(TEST_OUTPUT_TEST_FILE), "Test file was not created."

    # Read the output files
    train_df = pd.read_csv(TEST_OUTPUT_TRAIN_FILE)
    test_df = pd.read_csv(TEST_OUTPUT_TEST_FILE)
    original_df = pd.read_csv(TEST_INPUT_FILE)

    # Check if the dataframes are not empty
    assert not train_df.empty, "Training dataframe is empty."
    assert not test_df.empty, "Test dataframe is empty."

    # Check the length of the dataframes
    assert len(train_df) + len(test_df) == len(original_df), "Total length of split dataframes does not match original."

    # Check the split ratio
    expected_train_length = int(len(original_df) * 0.8)  # As per test_size=0.2
    expected_test_length = len(original_df) - expected_train_length
    assert len(train_df) == expected_train_length, "Length of training set is not as expected."
    assert len(test_df) == expected_test_length, "Length of test set is not as expected."

# Test with an empty input path
def test_empty_input_path():
    input_file = ""
    with pytest.raises(FileNotFoundError) as custom_string:
        split_data(input_file, TEST_OUTPUT_TRAIN_FILE, TEST_OUTPUT_TEST_FILE, test_size=0.2, random_state=123)
    assert str(custom_string.value), "Please provide an input file"


if __name__ == "__main__":
    test_split_data()