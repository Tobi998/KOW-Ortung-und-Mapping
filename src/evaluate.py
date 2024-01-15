"""
This model contains methods to evaluate the accuracy of the graphs generatet by this program
"""

import matplotlib.pyplot as plt
import pandas as pd
def calculate_distance_first_last_point():
    """
    Calculates the distance between the first and last point of the graph
    """

    #get first and last line of the plot
    first_line = plt.gca().get_lines()[0]
    last_line = plt.gca().get_lines()[-1]


    #get x and y values of the first point of the first line and last point of the last line
    first_point_x = first_line.get_xdata()[0]
    first_point_y = first_line.get_ydata() [0]
    last_point_x = last_line.get_xdata()[-1]
    last_point_y = last_line.get_ydata() [-1]

    #calculate the distance between the first and last point
    distance = ((first_point_x - last_point_x)**2 + (first_point_y - last_point_y)**2)**0.5	


    return distance


def evaluate_radius_diff_over_distance(df_calc, df_test):
    """
    Evaluates the difference between the radius of the calculated graph and the radius of the test graph

    :param df_calc: The calculated graph
    :param df_test: The test graph
    """

    #generate Comparrison table
    df_compare = compare_calc_test_graph(df_calc, df_test)
    
    #calculate average, sd, median, max and total radius differnce
    average = calc_average_from_df(df_compare)
    standard_deviation = calc_standard_deviation_from_df(df_compare)
    median = calc_median_from_df(df_compare)
    max = calc_max_from_df(df_compare)
    total = calc_total_from_df(df_compare)


    return df_compare, average, standard_deviation, median, max, total

def compare_calc_test_graph(df_calc, df_test):
    """
    Compares the calculated graph with the test graph, ba generating a table
    this table is composed of radius-calc, radius-test, radius-diff
    these values are calculatet for every odometerstep

    :param df_calc: The calculated graph
    :param df_test: The test graph
    """

    #get total odometersteps of the graph
    total_steps = df_calc['fixpoint_odometer_steps'].iloc[-1]


    compare_list = []


    #loop to add row for each step
    for step in range(total_steps + 1):
        #get the radius for the current step
        radius_calc = get_row_from_df_by_step(df_calc, step)['radius']
        radius_test = get_row_from_df_by_step(df_test, step)['radius']
        #calculate absolute differnce between the two radius
        radius_diff = abs(radius_calc - radius_test)
        #add values to list
        compare_list.append([radius_calc, radius_test, radius_diff])




    df_compare = pd.DataFrame(compare_list, columns=['radius-calc', 'radius-test', 'radius-diff'])

    return df_compare

def get_row_from_df_by_step(df, step):
    """
    Returns the last row from the dataframe where the step is bellow 'fixpoint_odometer_steps'

    :param df: The dataframe
    :param step: The step
    """

    #get the value from the last row where 'fixpoint_odometer_steps' is smaller or equal to step
    #use boolean mask to remove all rows where 'fixpoint_odometer_steps' is bigger than step
    #then take the last row of the remaining dataframe

    row = df.loc[df['fixpoint_odometer_steps'] <= step].iloc[-1]

    return row


def calc_average_from_df(df):
    """
    Calculates the average radius-diff from a dataframe

    :param df: The dataframe
    """


    return df['radius-diff'].mean()

def calc_standard_deviation_from_df(df):
    """
    Calculates the standard deviation of radius-diff from a dataframe
    """
    return df['radius-diff'].std()

def calc_median_from_df(df):
    """
    Calculates the median radius-diff from a dataframe
    """
    return df['radius-diff'].median()

def calc_max_from_df(df):
    """
    Calculates the max radius-diff from a dataframe
    """
    return df['radius-diff'].max()

def calc_total_from_df(df):
    """
    Calculates the total radius-diff from a dataframe
    """
    return df['radius-diff'].sum()