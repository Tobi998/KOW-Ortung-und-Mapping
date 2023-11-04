
import calculate_coordinates as cco
import user_interface as ui
import custome_calculations as cc
import pre_procces as pp
import plot as my_plt
import matplotlib.pyplot as plt
import numpy as np
import misc

x = [2671, 2640, 2570, 2511, 2490] 
y = [ 295.4, 360, 0,-360, -295.4] 

#x= [2570, 2485, 2663, 2653, 2515, 2630, 2518, 2525, 2610, 2600, 2535]
#y= [0, -233, 223, 190,-190, 225, -225, -252, 252, 323, -323]
f = cc.generate_2d_function(x, y)


ODOMETER_TO_MM_FACTOR = 2.9
#ODOMETER_TO_MM_FACTOR = 1.4

#Show function
"""
theta = np.linspace(2490, 2671, 100)
plt.plot(theta, f(theta), 'r-', label='radius')
plt.grid()
plt.show()
"""

#"""
path = ui.user_select_file()
csv_seperator = ui.ask_user_for_character("What seperator is used in the csv-file?")
print(csv_seperator)
df = pp.read_csv_file(path, seperator=csv_seperator)
user_wants_to_preprocces = ui.ask_user_true_false("Do you want to preprocces the data?")


#pre proccesing
if(user_wants_to_preprocces):
    columes_to_drop = ['board_time','server_time','odometer_speed','tie', 'fixpoint_hall','fixpoint_tie_steps','fixpoint_time','wifi','battery']
    df = pp.drop_unused_columes(df, columes_to_drop)
    df = pp.filter_dublicates(df)
    df = pp.reverse_dataframe(df)

pp.save_dataframe_to_csv(df, 'data/preprocces/preprocces_data')
#df.to_csv('data/filtered_data.csv', index=False)

#calculate coordinates
df = cco.add_radius_alpha_radian_to_df(df, f, ODOMETER_TO_MM_FACTOR)
pp.save_dataframe_to_csv(df,'data/postcalc/calculatet_data')




#post proccesing

print(df)
#plot
my_plt.plot_graph_with_semi_circle(df)

my_plt.save_plot('data/plot/plot_'+misc.get_timestamp()+'.png')

my_plt.show_plot()

#"""




