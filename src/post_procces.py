"""
This file contains the post processing functions
"""
import pandas as pd
import numpy as np
def map_low_radius_to_0(df, threshold):
    """
    Maps all values in the colume radius which are lower than the threshold to 0
    also maps alpha to 0 in the affected rows

    :param df: The dataframe which contains the radius colume
    :param threshold: The minimum threadhold for a radius to not be mapped to 0
    """


    #use a bool-mask to check which rows have to be changed
    #bool-mask is simply a boolean array
    mask = df['radius'] < threshold
    #use mask in loc to only change rows where the mask vaklue is true
    df.loc[mask, 'radius'] = 0
    df.loc[mask, 'alpha'] = 0
    
    return df

#drüberschauen
def map_to_closest_radius(df, radius_list):
    """
    Maps all values in the colume radius to the closest value in radius_list
    also maps alpha to 0 in the affected rows

    :param df: The dataframe which contains the radius colume
    :param radius_list: A list of radius values
    """

    
    return df



def mark_unstable_values(df, range, threshold):
    """
    Marks unstable values in the dataframe by looking if preciding values withing range have
    a radius that deviates by more than the threshold
    range here means within a certain number of fixpoint_odometer_steps not rows
    """
    #create a new colume unstable
    df['stable'] = 1

    #go through the dataframe
    for index, row in df.iterrows():
        #use mask to get all rows with a fixpoint_odometer_steps within
        # row['fixpoint_odometer_steps'] and row['fixpoint_odometer_steps'] - range
        mask = (df['fixpoint_odometer_steps'] <= row['fixpoint_odometer_steps']) & (df['fixpoint_odometer_steps'] >= row['fixpoint_odometer_steps'] - range)
        #get the highest deviiation of preciding rows from the current row
        max_deviation = (df.loc[mask, 'radius'] - row['radius']).abs().max()

        #if the deviation is higher than the threshold mark the row as unstable
        if(max_deviation > threshold):
            df.loc[index, 'stable'] = 0





    return df

def replace_unstable_values(df):
    """
    Replaces unstable values in the dataframe
    """
    
    #remove radius in  all unstable rows
    df['radius'] = df['radius'].where(df['stable'] == 1)

    df['radius'] = df['radius'].bfill()

    return df

def exponential_smoothin(df, col_name, alpha):
    """
    Smooths the values in the dataframe using exponential smoothing
    """
    return 0