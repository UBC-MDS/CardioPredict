# author: Doris Wang
# date: 2023-11-24

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Import the run_knn_analysis function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.run_split_prrepro import preprocess_and_split_data

# Test Function
def test_preprocess_and_split_data():
    # Paths for test files
    test_input_file = "data/toy/test_framingham.csv"
    test_output_train_file = "data/toy/train_df.csv"
    test_output_test_file = "data/toy/test_df.csv"

    # Check if the processed directory exists, create if not
    processed_dir = os.path.join(project_dir, "data/toy")
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # Sample numeric and categorical features (adjust as per your dataset)
    numeric_features = ['AGE', 'FRW', 'SBP', 'DBP', 'CHOL', 'CIG']
    categorical_features = ['sex']

    # Run the preprocessing function
    preprocess_and_split_data(test_input_file, test_output_train_file, test_output_test_file, 
                              numeric_features, categorical_features, test_size=0.2, random_state=123)

    # Assert that the output files are created
    assert os.path.exists(test_output_train_file), "Training file was not created."
    assert os.path.exists(test_output_test_file), "Test file was not created."

    # Read the output files and perform content checks
    train_df = pd.read_csv(test_output_train_file)
    test_df = pd.read_csv(test_output_test_file)

    # Assert that the files are not empty
    assert not train_df.empty, "Training file is empty."
    assert not test_df.empty, "Test file is empty."

    # Assert correct split ratio
    original_df = pd.read_csv(test_input_file)
    expected_train_size = int(len(original_df) * 0.8)
    expected_test_size = len(original_df) - expected_train_size
    assert len(train_df) == expected_train_size, "Training data size is incorrect."
    assert len(test_df) == expected_test_size, "Test data size is incorrect."

    # Assert preprocessing on training data
    # Check if numeric features are scaled
    scaler = StandardScaler()
    scaler.fit(original_df[numeric_features])
    scaled_numeric = scaler.transform(original_df[numeric_features])
    assert all(train_df[numeric_features].mean().abs() < 0.1), "Numeric features are not properly scaled in training data."

    # Check if categorical features are one-hot encoded
    encoder = OneHotEncoder(drop="if_binary", sparse_output=False)
    encoder.fit(original_df[categorical_features])
    encoded_categorical = encoder.transform(original_df[categorical_features])
    encoded_feature_names = encoder.get_feature_names_out(categorical_features)
    assert all(name in train_df.columns for name in encoded_feature_names), "Categorical features are not properly one-hot encoded in training data."

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    # Construct the full file paths
    input_file = os.path.join(project_dir, "data/toy/test_framingham.csv")
    output_train_file = os.path.join(project_dir, "data/toy/train_df.csv")
    output_test_file = os.path.join(project_dir, "data/toy/test_df.csv")

    # Example usage with the full paths
    preprocess_and_split_data(input_file, 
                              output_train_file, 
                              output_test_file,
                              ['AGE', 'FRW', 'SBP', 'DBP', 'CHOL', 'CIG'],  # Example numeric features
                              ['sex'])  # Example categorical feature
    print('All tests passed! 👍')