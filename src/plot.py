"""
This module containes functions that will take a pandas dataframe with x and y values
and plot a graph based on them.
It also contains functions to display other colums of the dataframe as a heat map.
"""

import matplotlib.pyplot as plt
import numpy as np


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

def plot_line(length, center_x, center_y, offset_alpha):
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


    alpha_rad = np.radians(offset_alpha)

    line_x_rotatet = line_x * np.cos(alpha_rad) - line_y * np.sin(alpha_rad)
    line_y_rotatet = line_x * np.sin(alpha_rad) + line_y * np.cos(alpha_rad)



    line_x_final = line_x_rotatet + center_x
    line_y_final = line_y_rotatet + center_y

    plt.plot(line_x_final, line_y_final, color='r', linewidth=2)

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




        if(left_turn * row['alpha'] < 0): #negative "left_turn * alpha" indicates switch from left to right turn and vise versa
            center_x, center_y, offset_alpha = adjust_center_and_offset_change_turn(center_x, center_y, offset_alpha, prev_radius)
            left_turn = -left_turn

        if(row['radius'] != prev_radius):
    
            center_x, center_y = adjust_center_new_radius(center_x, center_y, offset_alpha, prev_radius, row['radius'], left_turn)
            prev_radius = row['radius']
        

        if(row['radius'] == 0):
            plot_line(row['radian'], center_x, center_y, offset_alpha)
            center_x +=  - row['radian'] * np.sin(np.radians(offset_alpha))
            center_y +=  row['radian'] * np.cos(np.radians(offset_alpha))
        else:
            plot_semi_circle(row['radius'], row['alpha'], center_x, center_y, offset_alpha)
            offset_alpha += row['alpha']

    return 0

def adjust_center_new_radius(center_x, center_y, offset_alpha, radius_old, radius_new, left_turn):
    diff = left_turn* (abs(radius_old) - abs(radius_new))

    #print("Input",diff, offset_alpha)
    diff_x = diff * np.cos(np.radians(offset_alpha))
    diff_y = diff * np.sin(np.radians(offset_alpha))
    new_center_x = center_x + diff_x
    new_center_y = center_y + diff_y
    #print("center:",new_center_x, new_center_y)
    return new_center_x, new_center_y


def adjust_center_and_offset_change_turn(center_x, center_y, offset_alpha, radius):

    #Add or subtract 180 degrees to offset_alpha
    new_offset_alpha = offset_alpha

    #Mirror center through latest point on circle
    mirrorpoint = (center_x + radius * np.cos(np.radians(offset_alpha)), center_y + radius * np.sin(np.radians(offset_alpha)))
    mirrorvector = (mirrorpoint[0] - center_x, mirrorpoint[1] - center_y)
    new_center_x = center_x + 2 * mirrorvector[0]
    new_center_y = center_y + 2 * mirrorvector[1]


    #print("Old:",center_x,center_x,offset_alpha, " New:",new_center_x,new_center_y,new_offset_alpha)
    return new_center_x, new_center_y, new_offset_alpha



def show_plot():
    plt.show()

def save_plot(path):
    """
    Saves current plot to a png-file

    :param path: The path to save the file to
    """

    plt.savefig(path)


