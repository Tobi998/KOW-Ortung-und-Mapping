"""
This file contains the post processing functions
"""
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
from pykalman import KalmanFilter
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
def map_to_closest_value(df, column_name, value_list):
    """
    Maps all values in the colume_name to the closest value in value_list
    also maps alpha to 0 in the affected rows

    :param df: The dataframe which contains the radius colume
    :param radius_list: A list of values
    """

    #create a funtkion that gets the nearest value in value list
    def get_nearest_value(value):
        #get index by claculating absoulute differnce and getting the index of the min value wioth argmin
        index = (np.abs(value_list - value)).argmin()
        return value_list[index]

    df[column_name] = df[column_name].apply(get_nearest_value)


    
    return df



def mark_unstable_values(df, range, threshold, column_name):
    """
    Marks unstable values in the dataframe by looking if preciding values withing range have
    a radius that deviates by more than the threshold
    range here means within a certain number of fixpoint_odometer_steps not rows
    """
    #create a new colume unstable
    df['unstable'] = 0

    #go through the dataframe
    for index, row in df.iterrows():
        #use mask to get all rows with a fixpoint_odometer_steps within
        # row['fixpoint_odometer_steps'] and row['fixpoint_odometer_steps'] - range
        mask = (df['fixpoint_odometer_steps'] <= row['fixpoint_odometer_steps']) & (df['fixpoint_odometer_steps'] >= row['fixpoint_odometer_steps'] - range)
        #get the highest deviiation of preciding rows from the current row
        max_deviation = (df.loc[mask, column_name] - row[column_name]).abs().max()

        #if the deviation is higher than the threshold mark the row as unstable
        if(max_deviation > threshold):
            df.loc[index, 'unstable'] = 1





    return df

def replace_unstable_values(df, column_name):
    """
    Replaces unstable values in the dataframe
    """
    
    #remove radius in  all unstable rows
    #where replaces all values where the condition is false with nan
    df[column_name] = df[column_name].where(df['unstable'] == 0)
    #fill the nan values with the next stable value
    df[column_name] = df[column_name].bfill()
    #fill the nan values with the last stable value in case the last rows in the df are unstalbe
    df[column_name] = df[column_name].ffill()
    return df

def exponential_smoothing(df, col_name, alpha):
    """
    Smooths the values in the dataframe using exponential smoothing
    """

    df[col_name] = df[col_name].ewm(alpha).mean()

    return df

def moving_averge(df, col_name, window):
    """
    Smooths the values in the dataframe using moving average
    """

    df[col_name] = df[col_name].rolling(window).mean()

    return df

def moving_averge_with_dynamic_window(df, col_name):
    """
    Smooths the values in the dataframe using moving average
    Rather than using a static window size a window always gos from one stable value till the next unstable value
    """

    #create windows by creating groups of stable values
    #for this first add a colume group with a numbber that increments every time a value is unstalbe
    #series of stable values will be in their own group with unstable values each having one to them selves
    df['group'] = df['unstable'].cumsum()

    #calculate the averagew for each group and apply it to every row in the group
    df[col_name] = df.groupby('group')[col_name].transform('mean')


    return df


def savgol_smoothing(df, col_name, window, polyorder):
    """
    Smooths the values in the dataframe using savgol_filter
    """

    df[col_name] = savgol_filter(df[col_name], window, polyorder)

    return df


def summarize_curves(df):
    """
    Summerizes the curve representation of a graph by adding up all rows with the same radius
    """

    #group again
    #when radius changes the groupnumber counts up by one creating groupes for each curve
    df['group'] = (df['radius']!=df['radius'].shift()).cumsum()


    #use groupby and aggregate to summerize all the rows bellonging to the same group

    df_summery = df.groupby('group').agg({'alpha': 'sum','radian': 'sum','radius': 'first','fixpoint_odometer_steps': 'last'}).reset_index()

    return df_summery