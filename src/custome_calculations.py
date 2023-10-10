"""
This moduale contains mathematical functions which are used
by calculate_coordinates to calculate x and y values for each
messurement.
"""
import numpy as np
from scipy.interpolate import interp1d

def calculate_adjacent_side(alpha, hypothenuse):
    """
    Calculates the adjacent side of a rectangular triangle

    :param alpha: The angle between the adjacent side and the hypothenuse
    :param hypothenuse: The lenght of the hypothenuse of the rectangular triangle
    :return: The lenght of the adjacent side
    """

    if alpha >= 90 or alpha <= 0:
        raise ValueError("The angle must be between 0 and 90 degrees")
    
    return np.cos(np.radians(alpha)) * hypothenuse

def calculate_opposit_side(alpha, hypothenuse):
    """
    Calculates the opposite side of a rectangular triangle

    :param alpha: The angle between the adjacent side and the hypothenuse
    :param hypothenuse: The lenght of the hypothenuse of the rectangular triangle
    :return: The lenght of the opposite side
    """
    
    if alpha >= 90 or alpha <= 0:
        raise ValueError("The angle must be between 0 and 90 degrees")
    
    return np.sin(np.radians(alpha) ) * hypothenuse


def calculate_alpha(circle_radius, arc_in_mm):
    """
    Calculates the angle of a circular arc

    :param circle_radius: The radius of the circle
    :param arc_in_steps: The lenght of the arc in mm
    
    """

    if circle_radius <= 0:
        raise ValueError("The radius of the circle must be greater than zero")
    
    return arc_in_mm  * 180 / (np.pi * circle_radius)


def generate_2d_function(x, y):
    """
    Generates a 2d function from two arrays
    """
    return interp1d(x, y, kind='cubic', fill_value='extrapolate')


def calculate_vektor_kow():
    """
    Calculates the vektor between two points
    """
    return 0