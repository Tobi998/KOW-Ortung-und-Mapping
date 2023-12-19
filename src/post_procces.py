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