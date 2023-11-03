"""
This module containes functions that will take a pandas dataframe with x and y values
and plot a graph based on them.
It also contains functions to display other colums of the dataframe as a heat map.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def plot_graph(x, y):
    """
    This function takes x and y values
    and plots a graph based on them.

    :param x: The x values
    :param y: The y values
    :return: None
    """
    plt.plot(x, y)
    plt.show()

def plot_semi_circle(radius, alpha, center_x, center_y, offset_alpha):
    """
    Adds a semi circle to a plot.

    :param radius: The radius of the semi circle
    :param alpha: The angle of the semi circle
    :param center_x: The x coordinate of the center of the semi circle
    :param center_y: The y coordinate of the center of the semi circle
    :param offset_alpha: The base angle of the semi circle
    """

    alpha_rad = np.radians(alpha)  
    offset_alpha_rad = np.radians(offset_alpha)  
    theta = np.linspace(offset_alpha_rad, offset_alpha_rad + alpha_rad, 100)

    x = center_x + radius * np.cos(theta)  
    y = center_y + radius * np.sin(theta)  

    plt.plot(x, y, color='r', linewidth=2)
    return 0

def plot_line(radius, length, center_x, center_y, offset_alpha, left_turn):
    """
    Adds a line to a plot.
    this line is added as an extension to a semi-circle.

    :param radius: The radius of the semi circle
    :param length: The length of the line
    :param center_x: The x coordinate of the center of the semi circle
    :param center_y: The y coordinate of the center of the semi circle
    :param offset_alpha: The base angle of the semi circle
    """

    line_x = np.array([0,0]) 
    line_y = np.array([0,length]) 
    offset_alpha_rad = np.radians(offset_alpha)
    if(left_turn == -1):
        theta = np.radians(offset_alpha-180)
    else:
        theta = np.radians(offset_alpha)

    line_x_rotatet = line_x * np.cos(theta) - line_y * np.sin(theta)
    line_y_rotatet = line_x * np.sin(theta) + line_y * np.cos(theta)

    line_x_final = line_x_rotatet + center_x + radius * np.cos(offset_alpha_rad)
    line_y_final = line_y_rotatet + center_y + radius * np.sin(offset_alpha_rad)

    plt.plot(line_x_final, line_y_final, color='r', linewidth=2)

    #line_start = (radius + center_x, center_y)
    #line_stop = (radius + center_x, length + center_y)
    return 0


def plot_graph_with_semi_circle(df):
    """
    Plots a graph by addint semi circles and straight lines to a plot

    :param df: The dataframe to plot, regires the datframe to have
                to have radius, alpha, and radiant colums
    """

    left_turn = 1 #1 for left turn, -1 for right turn
    center_x, center_y = 0, 0
    offset_alpha = 0
    prev_radius= df.iloc[0]['radius']

    plt.gca().set_aspect('equal', adjustable='box')  # Make the plot aspect ratio equal
    
    for index, row in df.iterrows(): #don't remove index, otheerwise it will not work
        #print(center_x, center_y, offset_alpha, prev_radius)
        #  
        if(left_turn * row['alpha'] < 0): #1 * negative alpha indicates switch from left to right turn and vise versa
            center_x, center_y, offset_alpha = adjust_center_and_offset_change_turn(center_x, center_y, offset_alpha, prev_radius, left_turn)
            left_turn = -left_turn

        if(row['radius'] != prev_radius):
    
            center_x, center_y = adjust_center_new_radius(center_x, center_y, offset_alpha, prev_radius, row['radius'])
            prev_radius = row['radius']
        

        if(row['alpha'] == 0):
            plot_line(row['radius'], row['radian'], center_x, center_y, offset_alpha, left_turn)
            center_x += - left_turn * row['radian'] * np.sin(np.radians(offset_alpha))
            center_y += left_turn   * row['radian'] * np.cos(np.radians(offset_alpha))
        else:
            plot_semi_circle(row['radius'], row['alpha'], center_x, center_y, offset_alpha)
            offset_alpha += row['alpha']


    return 0

def adjust_center_new_radius(center_x, center_y, offset_alpha, radius_old, radius_new):
    diff = radius_old - radius_new

    #print("Input",diff, offset_alpha)
    diff_x = diff * np.cos(np.radians(offset_alpha))
    diff_y = diff * np.sin(np.radians(offset_alpha))
    new_center_x = center_x + diff_x
    new_center_y = center_y + diff_y
    #print("center:",new_center_x, new_center_y)
    return new_center_x, new_center_y


def adjust_center_and_offset_change_turn(center_x, center_y, offset_alpha, radius, left_turn):


    #Mirror center through latest point on circle
    mirrorpoint = (center_x + radius * np.cos(np.radians(offset_alpha)), center_y + radius * np.sin(np.radians(offset_alpha)))
    mirrorvector = (mirrorpoint[0] - center_x, mirrorpoint[1] - center_y)
    new_center_x = center_x + 2 * mirrorvector[0]
    new_center_y = center_y + 2 * mirrorvector[1]
    #Add or subtract 180 degrees to offset_alpha
    new_offset_alpha = offset_alpha + left_turn * 180

    print("Old:",center_x,center_x,offset_alpha, " New:",new_center_x,new_center_y,new_offset_alpha)
    return new_center_x, new_center_y, new_offset_alpha

def plot_heat_map(x, y, z):
    """
    This function takes x and y values
    and plots a heat map based on them.

    :param x: The x values
    :param y: The y values
    :param z: The z values
    :return: None
    """
    plt.scatter(x, y, c=z)
    plt.show()



plt.gca().set_aspect('equal', adjustable='box')  # Make the plot aspect ratio equal


#print(center_x, center_y)
df = pd.read_csv('data/test2.csv')
plot_graph_with_semi_circle(df)
plt.show()