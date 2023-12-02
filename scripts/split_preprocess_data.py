# scripts/preprocess_data.py
# author: Doris Wang
# date: 2023-11-30

import click
import os
import pickle
import pandas as pd
import numpy as np
from sklearn import set_config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

@click.command()
@click.option('--input-file', required=True,
              type=click.Path(exists=True), help="The path to the raw data CSV file.")
@click.option('--split-dir', required=True,
              type=click.Path(), help="The directory where the splitted data should be saved.")
@click.option('--preprocess-dir', required=True,
              type=click.Path(), help="The directory where the processed data and object should be saved.")
@click.option('--preprocessor-to', type=str, help="Path to directory where the preprocessor object will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)

def main(input_file, split_dir, preprocess_dir, preprocessor_to, seed):
    '''This script splits the raw data into train and test sets, 
    and then preprocesses the data to be used in exploratory data analysis.
    It also saves the preprocessor to be used in the model training script.'''
    np.random.seed(seed)
    set_config(transform_output="pandas")

    # Ensure output directory exists
    if not os.path.exists(split_dir):
        os.makedirs(split_dir)

    # Load the data
    df = pd.read_csv(input_file)

    # Split the data into train and test sets
    train_df, test_df = train_test_split(df, test_size=0.2)

    # Save the processed data
    train_df.to_csv(os.path.join(split_dir, 'train_data.csv'), index=False)
    test_df.to_csv(os.path.join(split_dir, 'test_data.csv'), index=False)

    # Separate target value form train and test set 
    X_train = train_df.drop(columns="disease")
    y_train = train_df["disease"]

    X_test = test_df.drop(columns=["disease"])
    y_test = test_df["disease"]

    # Save the splitted data
    X_train.to_csv(os.path.join(split_dir, 'X_train.csv'), index=False)
    X_test.to_csv(os.path.join(split_dir, 'X_test.csv'), index=False)
  
    y_train.to_csv(os.path.join(split_dir, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(split_dir, 'y_test.csv'), index=False)

    print(f"Processed data saved to {split_dir}")


    # Perform pre-processing
    numeric_features = X_train.select_dtypes(include='number').columns.tolist()
    categorical_features = ["sex"]

    numeric_pipe = make_pipeline(
        SimpleImputer(strategy = "median"), StandardScaler()
    )

    preprocessor = make_column_transformer(    
        (numeric_pipe, numeric_features),  
        (OneHotEncoder(drop="if_binary", sparse_output = False), categorical_features)
)
    

    pickle.dump(preprocessor, open(os.path.join(preprocessor_to, "preprocessor.pickle"), "wb"))

    preprocessor.fit(X_train)

    # Convert the transformed data back to DataFrames to use the to_csv method
    X_train_transformed = pd.DataFrame(preprocessor.transform(X_train), columns=preprocessor.get_feature_names_out())
    X_test_transformed = pd.DataFrame(preprocessor.transform(X_test), columns=preprocessor.get_feature_names_out())

    X_train_transformed.to_csv(os.path.join(preprocess_dir, "X_train_transformed.csv"), index=False)
    X_test_transformed.to_csv(os.path.join(preprocess_dir, "X_test_transformed.csv"), index=False)

if __name__ == '__main__':
    main()

# python scripts/split_preprocess_data.py --input-file data/raw/framingham.csv --split-dir data/processed/ --preprocess-dir data/processed/ --preprocessor-to results/models/