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

def calculate_vektor_in_circle(radius, alpha):
    """
    Calculates the vektor between two points in a circle

    :param radius: The radius of the circle
    :param alpha: The angle between the two points
    """
    if radius <= 0:
        raise ValueError("The radius of the circle must be greater than zero")

    #covering all cases from 0 to 360 degrees
    if alpha== 0 or alpha == 360:
        return 0, 0
    elif 0 < alpha < 90:
        return calculate_adjacent_side(alpha, radius)-radius, calculate_opposit_side(alpha, radius)
    elif alpha == 90:
        return -radius, radius
    elif 90 < alpha < 180:
        return -calculate_opposit_side(alpha-90, radius)-radius, calculate_adjacent_side(alpha-90, radius)
    elif alpha == 180:
        return -2*radius, 0
    elif 180 < alpha < 270:
        return -calculate_adjacent_side(alpha-180, radius)-radius, -calculate_opposit_side(alpha-180, radius)
    elif alpha == 270:
        return -radius, -radius
    elif 270 < alpha < 360:
        return calculate_opposit_side(alpha-270, radius)-radius, -calculate_adjacent_side(alpha-270, radius)
    else:
        raise ValueError("The angle must be between 0 and 360 degrees. Current Angel is " + str(alpha)+
                         ". Current Radius is " + str(radius))

def calculate_alpha(circle_radius, arc_in_mm):
    """
    Calculates the angle of a circular arc

    :param circle_radius: The radius of the circle
    :param arc_in_steps: The lenght of the arc in mm
    
    """

    if circle_radius <= 0:
        raise ValueError("The radius of the circle must be greater than zero. Radius is " + str(circle_radius))
    if arc_in_mm <= 0:
        raise ValueError("The lenght of the arc must be greater than zero. Arc lenght is " + str(arc_in_mm))
    return arc_in_mm  * 180 / (np.pi * circle_radius)

def generate_2d_function(x, y):
    """
    Generates a 2d function from two arrays

    :param x: x values of the function
    :param y: y values of the function
    """
    return interp1d(x, y, kind='cubic',fill_value='extrapolate')

def calculate_radius(steering, hall__to_radius_function):
    """
    Calculates the radius of the rail based on the steering voltage

    :param steering: The voltage induced by the hall sensor
    :param hall__to_radius_function: A function which maps steering to thr radius of the rail
    """
    return hall__to_radius_function(steering)

def calculate_vektor_to_next_point(steering, odometer_steps_point, odometer_steps_next_point, hall__to_radius_function, ODOMETER_TO_MM_FACTOR):
    """
    Calculates the vektor to the next messurment of the KOW

    :param steering: The voltage induced by the hall sensor
    :param odometer_steps_point: The odometer steps of the current point
    :param odometer_steps_next_point: The odometer steps of the next point
    :param hall__to_radius_function: A function which maps steering to thr radius of the rail
    :param ODOMETER_TO_MM_FACTOR: A factor which maps the odometer steps to mm
    """
    print('A')
    radius = hall__to_radius_function(steering)
    radius = round(float(radius), 2)
    delta_steps = odometer_steps_next_point - odometer_steps_point
    if(delta_steps < 0):
        raise ValueError("The odometer steps of the next point must be greater than the odometer steps of the current point."+
                         "Currently Point="+str(odometer_steps_point)+", Next Point="+str(odometer_steps_next_point))
    if(radius == 0):
        return 0, delta_steps * ODOMETER_TO_MM_FACTOR
    elif(radius < 0):
        angle_alpha = calculate_alpha(-radius, delta_steps * ODOMETER_TO_MM_FACTOR)
        x, y = calculate_vektor_in_circle(-radius, angle_alpha)
        return -x, y
    else:
        angle_alpha = calculate_alpha(radius, delta_steps * ODOMETER_TO_MM_FACTOR)
        x, y = calculate_vektor_in_circle(radius, angle_alpha)
        return x, y

def calculate_circle_to_next_point(steering, odometer_steps_point, odometer_steps_next_point, hall__to_radius_function, ODOMETER_TO_MM_FACTOR):
    """
    Calculates the partial circle to the next messurment of the KOW
    This is composed of radius, alpha and radians
    In case of a straightr line the radius is 0 and alpha is 0
    radians becomes the distance to the next point

    :param steering: The voltage induced by the hall sensor
    :param odometer_steps_point: The odometer steps of the current point
    :param odometer_steps_next_point: The odometer steps of the next point
    :param hall__to_radius_function: A function which maps steering to thr radius of the rail
    :param ODOMETER_TO_MM_FACTOR: A factor which maps the odometer steps to mm
    """
    radius = hall__to_radius_function(steering)
    radius = round(float(radius), 2)
    delta_steps = odometer_steps_next_point - odometer_steps_point
    if(delta_steps < 0):
        raise ValueError("The odometer steps of the next point must be greater than the odometer steps of the current point."+
                         "Currently Point="+str(odometer_steps_point)+", Next Point="+str(odometer_steps_next_point))
    if(radius == 0):
        return 0, 0, delta_steps * ODOMETER_TO_MM_FACTOR
    elif(radius < 0):
        #negative radius means a right turn
        angle_alpha = calculate_alpha(-radius, delta_steps * ODOMETER_TO_MM_FACTOR)
        return radius, -angle_alpha, delta_steps * ODOMETER_TO_MM_FACTOR
    else:
        angle_alpha = calculate_alpha(radius, delta_steps * ODOMETER_TO_MM_FACTOR)
        return radius, angle_alpha, delta_steps * ODOMETER_TO_MM_FACTOR