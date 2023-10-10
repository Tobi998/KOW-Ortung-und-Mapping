"""
This module containes functions used to read date from a csv-file
and turn it to a pandas dataframe that can be used by other modules.
"""

import pandas as pd

def read_csv_file(file_path):
    """
    This function takes a file path of a csv-file
    and returns it content as a pandas dataframe

    :param file_path: The path to the csv-file
    :return: A pandas dataframe containing the content of the csv-file
    """
    df = pd.read_csv(file_path)
    return df   
