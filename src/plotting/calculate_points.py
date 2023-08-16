import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

ODOMETER_TO_MM_FACTOR= 1.4
TIE_TO_MM_FACTOR = 3.7

path_dir = 'src\data\outer_round1_forward.csv'

messurments = pd.read_csv(path_dir)
messurments = messurments.dropna(how="all")



hall_sensor_messurment_mv = [2671, 2640, 2560, 2511, 2490]
curve_radius_mm = [ 295.4, 360, 0,-360, -295.4] 
#positiv values indicate a left turn, negativ values indicate a right turn

hall__to_radius_function  =interp1d(hall_sensor_messurment_mv, curve_radius_mm, kind='cubic', fill_value='extrapolate')


def pythagoras_calc_an_und_gegenkatete(hypothenuse, alpha):
    return [np.cos(np.radians(alpha)) * hypothenuse, np.sin(np.radians(alpha)) * hypothenuse]

def calculate_angle_alpha(circle_radius, arc_in_steps):
    return arc_in_steps * ODOMETER_TO_MM_FACTOR * 180 / (np.pi * circle_radius)



def calculate_vektor_to_next_point(steering, odometer_steps_point, 
                                   odometer_steps_next_point):
    radius = hall__to_radius_function(steering)
    delta_steps = odometer_steps_next_point - odometer_steps_point
    angle_alpha = calculate_angle_alpha(radius, delta_steps)
    ankatete, gegenkatete = pythagoras_calc_an_und_gegenkatete(radius, angle_alpha)
    return [ankatete -radius,gegenkatete]
    



#Vektoren zwischen Punkten berechnen

test = calculate_vektor_to_next_point(2671, 30, 70)


messurments['vektors_to_next_point_x' ], messurments['vektors_to_next_point_y']= calculate_vektor_to_next_point(messurments['steering'], messurments['fixpoint_odometer_steps'],
                               messurments['fixpoint_odometer_steps'].shift(fill_value=0))

"""
def calculate_vektor_to_next_point(p1,p2):
    return p2-p1

messurments['vektors_to_next_point' ] = calculate_vektor_to_next_point(messurments['fixpoint_odometer_steps'],
                                                                       messurments['fixpoint_odometer_steps'].shift(fill_value=0))
"""
print(messurments['vektors_to_next_point_x'], messurments['vektors_to_next_point_y'])


points = pd.DataFrame()
points['x'] =  messurments['vektors_to_next_point_x']
points['y'] =  messurments['vektors_to_next_point_y']



print(points['x'])