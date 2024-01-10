"""
This module containes functions that will take a pandas dataframe and
add x and y values to each row.
This assumes that the dataframe containes messurments of the KOW.
"""

import numpy as np
import pandas as pd
from custome_calculations import calculate_vektor_to_next_point, calculate_circle_to_next_point

#unused remove later
def add_x_and_y_to_df(df, hall__to_radius_function, ODOMETER_TO_MM_FACTOR ):
    """
    This function takes a pandas dataframe with KOW-Data and adds x and y values to each row.
    """
    df['x']=float(0)
    df['y']=float(0)
    #Method 1: Using a for loop
    for index in df.iterrows():
        if index == 0:
            df.at[index, 'x'] = 0
            df.at[index, 'y'] = 0
        else:
            x, y = calculate_vektor_to_next_point(df.at[index-1, 'steering'], 
                                                     df.at[index, 'fixpoint_odometer_steps'],
                                                     df.at[index-1, 'fixpoint_odometer_steps']
                                                     , hall__to_radius_function, ODOMETER_TO_MM_FACTOR)
            df.at[index, 'x'] = df.at[index-1, 'x'] + x
            df.at[index, 'y'] = df.at[index-1, 'y'] + y

    #Methode 2: Using a lambda function
    return df
    

def add_radius_alpha_radian_to_df(df, hall__to_radius_function, ODOMETER_TO_MM_FACTOR ):
    """
    This function takes a pandas dataframe with KOW-Data and adds radius, alpha and radian values to each row.
    """
    df['radius']=float(0)
    df['alpha']=float(0)
    df['radian']=float(0)

    #iterrows solution
    for index in range(len(df)-1):
        radius, alpha, radian = calculate_circle_to_next_point(df.at[index, 'steering'], 
                                                     df.at[index, 'fixpoint_odometer_steps'],
                                                     df.at[index+1, 'fixpoint_odometer_steps']
                                                     , hall__to_radius_function, ODOMETER_TO_MM_FACTOR)
        df.at[index, 'radius'] = radius
        df.at[index, 'alpha'] = alpha
        df.at[index, 'radian'] = radian


    #vectorisation
    #pleas implement later
    return df