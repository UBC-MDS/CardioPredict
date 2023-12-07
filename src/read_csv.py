# src.read_csv.py
# author: Doris Wang
# date: 2023-11-30

import requests
import os
import pandas as pd

def download_data(url, filepath):
    """
    Downloads a CSV file from a given URL and saves it to a specified local path.

    This function checks if the URL is valid and points to a CSV file, creates the
    directory if it doesn't exist, downloads the file, and verifies that the 
    downloaded CSV is not empty. Raises errors for invalid URL, non-CSV content, 
    or empty files.

    Parameters:
    ----------
    url : str
        The URL of the CSV file to download. Must be a valid and accessible URL.
    filepath : str
        The local path where the downloaded file will be saved. If the directory
        in the path doesn't exist, it will be created.

    Raises:
    ------
    ValueError:
        - If the URL is invalid or inaccessible.
        - If the URL does not point to a CSV file.
        - If the downloaded CSV file is empty.

    Example:
    -------
    >>> download_data('https://example.com/data.csv', './data/my_data.csv')
    File downloaded successfully and saved to ./data/my_data.csv

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
