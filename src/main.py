
import calculate_coordinates as cco
import user_interface as ui
import custome_calculations as cc
import pre_procces as pp

path = ui.user_select_file()

df = pp.read_csv_file(path)


"""

df = df.drop('board_time', axis=1)
df = df.drop('server_time', axis=1)
df = df.drop('odometer_speed', axis=1)
df = df.drop('tie', axis=1)
df = df.drop('fixpoint_hall', axis=1)
df = df.drop('fixpoint_tie_steps', axis=1)
df = df.drop('fixpoint_time', axis=1)
df = df.drop('wifi', axis=1)
df = df.drop('battery', axis=1)

df = pp.filter_dublicates(df)
df = pp.reverse_dataframe(df)
"""
#print(df)
#print(df.iloc[0])
#df.to_csv('data/filtered_data.csv', index=False)


x = [2671, 2640, 2560, 2511, 2490]
y = [ 295.4, 360, 0,-360, -295.4]
f = cc.generate_2d_function(x, y)
ODOMETER_TO_MM_FACTOR = 1.4

#print(f(2569))
df = cco.add_radius_alpha_radian_to_df(df, f, ODOMETER_TO_MM_FACTOR)

print(df['alpha'].sum())
#print(df)
#df.to_csv('data/circles.csv', index=False)
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




