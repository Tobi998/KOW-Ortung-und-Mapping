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
    df = df.reset_index(drop=True)
    return df   


def filter_dublicates(df):
    """
    This function takes a pandas dataframe and removes all dublicates 
    based on fixpoint_odometer_steps
    

    :param df: The pandas dataframe
    :return: The pandas dataframe without dublicates
    """
    df = df.drop_duplicates(subset=['fixpoint_odometer_steps'], keep='first')
    #df = df[df['steering'].shift() != df['steering']]
    return df

def reverse_dataframe(df):
    """
    This function takes a pandas dataframe and reverses it

    :param df: The pandas dataframe
    :return: The reversed pandas dataframe
    """
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)
    return df