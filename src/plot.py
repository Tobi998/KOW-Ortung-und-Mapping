"""
This module containes functions that will take a pandas dataframe with x and y values
and plot a graph based on them.
It also contains functions to display other colums of the dataframe as a heat map.
"""

import matplotlib.pyplot as plt

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

def plot_semi_circle(radius, alpha, center_x, center_y, base_angle):
    return 0


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

#plot_graph([1,2,3,1,0], [1,2,3,5,2])

#plot_heat_map([1,2,3,1,0], [1,2,3,5,2], [1,2,3,5,2])