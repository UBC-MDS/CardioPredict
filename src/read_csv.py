# src.read_csv.py
# author: Doris Wang
# date: 2023-11-30

import requests
import os
import pandas as pd

def download_data(url, filepath):
    """
    Downloads a CSV file from a given URL and saves it to a specified local path.

    Parameters:
    ----------
    url : str
        The URL of the CSV file to download.
    filepath : str
        The local path to save the downloaded file.
    """
    response = requests.get(url)
    
    # Check if URL exists, if not raise an error
    if response.status_code != 200:
        raise ValueError('The URL provided does not exist or is inaccessible.')
    
    # Check if the URL points to a CSV file, if not raise an error
    content_type = response.headers.get('Content-Type')
    if 'csv' not in content_type:
        raise ValueError('The URL provided does not point to a valid CSV file.')

    # Check if the directory exists, if not, create it
    directory = os.path.dirname(filepath)
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=True)

    # Write the CSV file to the directory
    with open(filepath, 'wb') as file:
        file.write(response.content)

    # Verify that the CSV is not empty
    df = pd.read_csv(filepath)
    if df.empty:
        raise ValueError("The downloaded file is empty.")

    print(f"File downloaded successfully and saved to {filepath}")
