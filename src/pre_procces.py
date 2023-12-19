"""
This module containes functions used to read date from a csv-file
and turn it to a pandas dataframe that can be used by other modules.
"""

import pandas as pd
import datetime
def read_csv_file(file_path, seperator):
    """
    This function takes a file path of a csv-file
    and returns it content as a pandas dataframe

    :param file_path: The path to the csv-file
    :return: A pandas dataframe containing the content of the csv-file
    """
    df = pd.read_csv(file_path, sep=seperator)
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

def drop_unused_columes(df, columes_to_drop):
    """
    This function takes a pandas dataframe and removes all columes
    that are not used in the calculations

    :param df: The pandas dataframe
    :param columes_to_drop: A list of columes that should be removed
    :return: The pandas dataframe without unused columes
    """
    columes_to_drop = ['board_time','server_time','odometer_speed','tie',
                       'fixpoint_hall','fixpoint_tie_steps','fixpoint_time','wifi','battery']
    
    for col in columes_to_drop:
        if col in df.columns:
            df = df.drop(col, axis=1)
    """
    df = df.drop('board_time', axis=1)
    df = df.drop('server_time', axis=1)
    df = df.drop('odometer_speed', axis=1)
    df = df.drop('tie', axis=1)
    df = df.drop('fixpoint_hall', axis=1)
    df = df.drop('fixpoint_tie_steps', axis=1)
    df = df.drop('fixpoint_time', axis=1)
    df = df.drop('wifi', axis=1)
    df = df.drop('battery', axis=1)
    """


    return df

def save_dataframe_to_csv(df, path):
    """
    This function takes a pandas dataframe and saves it to a csv-file

    :param df: The pandas dataframe
    :param name: The name of the csv-file
    """
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")
    filename = path + "_" + timestamp + ".csv"
    df.to_csv(filename, index=False)


def filter_high_steering(df, threshold):
    """
    This function takes a pandas dataframe and removes all rows
    where the steering value is higher than the threshold

    :param df: The pandas dataframe
    :param threshold: The threshold value
    :return: The pandas dataframe without high steering values
    """
    #Create bool-mask with df['steering'] < threshold than filter all rows not meeting the condition
    df = df[df['steering'] < threshold]
    df = df.reset_index(drop=True)
    return df