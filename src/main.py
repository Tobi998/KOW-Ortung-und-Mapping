
import calculate_coordinates as cco
import user_interface as ui
import custome_calculations as cc
import pre_procces as pp
import post_procces as pop
import plot as my_plt
import matplotlib.pyplot as plt
import numpy as np
import misc
import config
import ast
import evaluate as ev

#x = [2671, 2640, 2570, 2511, 2490] 
#y = [ 295.4, 360, 0,-360, -295.4] 

x = ast.literal_eval(config.load_config('config.ini', 'DEFAULT', 'Hall_mv'))
y = ast.literal_eval(config.load_config('config.ini', 'DEFAULT', 'Radius_mm'))
#sort based on x (hall-sensore-voltage)
xy = sorted(zip(x, y))
x, y = zip(*xy)

f = cc.generate_2d_function(x, y)

"""
x_new = np.linspace(min(x), max(x), num=1000, endpoint=True)
y_new = f(x_new)

plt.plot(x_new, y_new, '-')
plt.show()

"""







#ODOMETER_TO_MM_FACTOR = 2.9
ODOMETER_TO_MM_FACTOR = float(config.load_config('config.ini', 'DEFAULT', 'ODOMETER_TO_MM_FACTOR'))

#Show function
"""
theta = np.linspace(2490, 2671, 100)
plt.plot(theta, f(theta), 'r-', label='radius')
plt.grid()
plt.show()
"""

#"""
path = ui.user_select_file()
#csv_seperator = ui.ask_user_for_character("What seperator is used in the csv-file?")

csv_seperator = config.load_config('config.ini', 'DEFAULT', 'CSV_Sepperator')
df = pp.read_csv_file(path, csv_seperator)
user_wants_to_preprocces = ui.ask_user_true_false("Do you want to preprocces the data?")


#pre proccesing
if(user_wants_to_preprocces):
    columes_to_drop = ['board_time','server_time','odometer_speed','tie', 'fixpoint_hall','fixpoint_tie_steps','fixpoint_time','wifi','battery']
    df = pp.drop_unused_columes(df, columes_to_drop)
    df = pp.filter_dublicates(df)
    df = pp.reverse_dataframe(df)
    df = pp.filter_high_steering(df, 3500)

pp.save_dataframe_to_csv(df, 'data/preprocces/preprocces_data')
#df.to_csv('data/filtered_data.csv', index=False)

#calculate coordinates
df = cco.add_radius_alpha_radian_to_df(df, f, ODOMETER_TO_MM_FACTOR)
pp.save_dataframe_to_csv(df,'data/postcalc/calculatet_data')




#post proccesing
df = pop.map_low_radius_to_0(df, 150)

pp.save_dataframe_to_csv(df, 'data/postprocces/postprocces_data')
#plot
my_plt.plot_graph_with_semi_circle(df)

my_plt.save_plot('data/plot/plot_'+misc.get_timestamp()+'.png')



#Evaluate
print("Abstand erster und letzter Punkt: ", ev.calculate_distance_first_last_point()) 

#Load df for comparrison
path_test = "data/compare_data/compare_data_outer_circle_1.csv"
seperator_test=','
df_test = pp.read_csv_file(path_test, seperator_test)
df_compare, average, standard_deviation, median, max, total = ev.evaluate_radius_diff_over_distance(df, df)
print("Average: ", average)
print("Standard deviation: ", standard_deviation)
print("Median: ", median)
print("Max: ", max)
print("Total: ", total)
print(df_test)
pp.save_dataframe_to_csv(df_compare,'data/evaluate/calculatet_data')


my_plt.show_plot()






