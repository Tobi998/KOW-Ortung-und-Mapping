import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

hall_sensor_messurment_mv = [2671, 2640, 2560, 2511, 2490]

curve_radius_mm = [ 295.4, 360, 0,-360, -295.4] 
#positiv values indicate a left turn, negativ values indicate a right turn

function=interp1d(hall_sensor_messurment_mv, curve_radius_mm, kind='cubic', fill_value='extrapolate')


x = np.linspace(2671, 2490, 100)
#x = np.linspace(2700, 2450, 100)
y = function(x)

#function(4000)

plt.scatter(x,y)
plt.show()