
import calculate_coordinates as cco
import user_interface as ui
import custome_calculations as cc
import pre_process as pp
import post_process as pop
import plot as my_plt
import misc
import config
import ast
import evaluate as ev
import numpy as np
import matplotlib.pyplot as plt


x = ast.literal_eval(config.load_config('config.ini', 'DEFAULT', 'Hall_mv'))
y = ast.literal_eval(config.load_config('config.ini', 'DEFAULT', 'Radius_mm'))
#sort based on x (hall-sensore-voltage)
xy = sorted(zip(x, y))
x, y = zip(*xy)




kind = config.load_config('config.ini', 'DEFAULT', 'interp_kind')

f = cc.generate_2d_function(x, y, kind)



"""
#Code used for Thesis remove for full release
x_new = np.linspace(min(x), max(x), num=1000, endpoint=True)
y_new = f(x_new)

plt.plot(x_new, y_new, '-')
plt.show()
"""











ODOMETER_TO_MM_FACTOR = float(config.load_config('config.ini', 'DEFAULT', 'ODOMETER_TO_MM_FACTOR'))


path = ui.user_select_file()



df = pp.read_csv_file(path)



#pre proccesing

columes_to_drop = ['board_time','server_time','odometer_speed','tie', 'fixpoint_hall','fixpoint_tie_steps','fixpoint_time','wifi','battery']
df = pp.drop_unused_columes(df, columes_to_drop)
df = pp.filter_dublicates(df)
df = pp.reverse_dataframe(df)
df = pp.filter_high_steering(df, 3500)
df = pp.filter_low_steering(df, 2000)



df = pop.mark_unstable_values(df, 10, 30, 'steering')


#df = pop.savgol_smoothing(df, 'steering', 30, 1)

#df = pop.exponential_smoothing(df,'steering', 0.9)

#df = pop.moving_averge_with_dynamic_window(df,'steering')


#df = pop.replace_unstable_values(df, 'steering')

mapping_values = np.array(x)

#df = pop.map_to_closest_value(df, 'steering', mapping_values)



pp.save_dataframe_to_csv(df, 'data/preprocces/preprocces_data')






#calculate coordinates
df = cco.add_radius_alpha_radian_to_df(df, f, ODOMETER_TO_MM_FACTOR)

#pp.save_dataframe_to_csv(df,'data/postcalc/calculatet_data')




#post proccesing
df = pop.map_low_radius_to_0(df, 200)





#pp.save_dataframe_to_csv(df, 'data/postprocces/postprocces_data')



my_plt.plot_graph_with_semi_circle(df)

my_plt.save_plot('data/plot/plot_'+misc.get_timestamp()+'.png')




eval = config.load_config_bool('config.ini', 'DEVELOPMENT', 'evaluate')

if eval:
    #Evaluate
    print("Abstand erster und letzter Punkt: ", ev.calculate_distance_first_last_point()) 

    #Load df for comparrison
    path_test = "data/compare_data/compare_data_track1.csv"

    df_test = pp.read_csv_file(path_test)
    df_compare, average, standard_deviation, median, max, total = ev.evaluate_radius_diff_over_distance(df, df_test)
    print("Average: ", average)
    print("Standard deviation: ", standard_deviation)
    print("Median: ", median)
    print("Max: ", max)
    print("Total: ", total)

    pp.save_dataframe_to_csv(df_compare,'data/evaluate/evaluate_data')

df = pop.summarize_curves(df)
pp.save_dataframe_to_csv(df, 'data/graph_summery/summery_data')

#plot


my_plt.show_plot()






