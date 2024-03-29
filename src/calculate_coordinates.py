"""
This module containes functions that will take a pandas dataframe and
add x and y values to each row.
This assumes that the dataframe containes messurments of the KOW.
"""


from custome_calculations import calculate_circle_to_next_point



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