# scripts/download_data.py
# author: Doris Wang
# date: 2023-11-30

import click
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read_csv import download_data

@click.command()
@click.option('--url')
@click.option('--filepath')

def main(url, filepath):
    """ Command-line function to download data from a specified URL and save it to a local path.
    
    URL: URL to the CSV file to be downloaded.
    FILEPATH: Local path where the CSV file will be saved.
    """
    download_data(url, filepath)
    print("Download completed.")

if __name__ == '__main__':
    main()


#python scripts/download_data.py --url "https://paulblanche.com/files/framingham.csv" --filepath "data/raw/framingham.csv"
