
import calculate_coordinates as cco
import user_interface as ui
import custome_calculations as cc
import pre_procces as pp
import matplotlib.pyplot as plt
import numpy as np
path = ui.user_select_file()

df = pp.read_csv_file(path)
x = [2671, 2640, 2560, 2511, 2490]
y = [ 295.4, 360, 0,-360, -295.4]
f = cc.generate_2d_function(x, y)
ODOMETER_TO_MM_FACTOR = 1.4


#Show function
"""
theta = np.linspace(2490, 2671, 100)
plt.plot(theta, f(theta), 'r-', label='radius')
plt.grid()
plt.show()
"""


columes_to_drop = ['board_time','server_time','odometer_speed','tie', 'fixpoint_hall','fixpoint_tie_steps','fixpoint_time','wifi','battery']
#pre proccesing
df = pp.drop_unused_columes(df, columes_to_drop)
df = pp.filter_dublicates(df)
df = pp.reverse_dataframe(df)

pp.save_dataframe_to_csv(df, 'preprocces_data', 'data\preprocces')
#df.to_csv('data/filtered_data.csv', index=False)

#calculate coordinates
df = cco.add_radius_alpha_radian_to_df(df, f, ODOMETER_TO_MM_FACTOR)
pp.save_dataframe_to_csv(df, 'calculatet_data', 'data\postcalc')
print(df)

#df.to_csv('data/filtered_data.csv', index=False)

#post proccesing


#plot







"""
df=df.iloc[::-1]
print(df)
x = [2671, 2640, 2560, 2511, 2490]
y = [ 295.4, 360, 0,-360, -295.4]
f = cc.generate_2d_function(x, y)
ODOMETER_TO_MM_FACTOR = 1.4
df = cco.add_x_and_y_to_df(df, f, ODOMETER_TO_MM_FACTOR)

ui.plot_x_y(df.x, df.y)
"""




