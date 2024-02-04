
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
save_df= config.load_config_bool('config.ini', 'DEVELOPMENT', 'save_dataframe')

path = ui.user_select_file()



df = pp.read_csv_file(path)



#pre proccesing

apply_unstable= config.load_config_bool('config.ini', 'REPLACEUNSTABLEVALUES', 'apply')
apply_svagol= config.load_config_bool('config.ini', 'SVAGOLFILTER', 'apply')
apply_exponential= config.load_config_bool('config.ini', 'EXPONENTIALSMOOTHING', 'apply')
apply_average= config.load_config_bool('config.ini', 'AVERAGEDYNAMICWINDOW', 'apply')
apply_mapping = config.load_config_bool('config.ini', 'POSTPROCESSINGGENERAL', 'map_to_closest')	

min_steering = float(config.load_config('config.ini', 'POSTPROCESSINGGENERAL', 'min_steering'))
max_steering = float(config.load_config('config.ini', 'POSTPROCESSINGGENERAL', 'max_steering'))



columes_to_drop = ['board_time','server_time','odometer_speed','tie', 'fixpoint_hall','fixpoint_tie_steps','fixpoint_time','wifi','battery']
df = pp.drop_unused_columes(df, columes_to_drop)
df = pp.filter_dublicates(df)
df = pp.reverse_dataframe(df)
df = pp.filter_high_steering(df, max_steering)
df = pp.filter_low_steering(df, min_steering)

if(apply_unstable or apply_average):
    unstable_range= float(config.load_config('config.ini', 'REPLACEUNSTABLEVALUES', 'range'))
    unstable_threshold = float(config.load_config('config.ini', 'REPLACEUNSTABLEVALUES', 'threshold'))

    df = pop.mark_unstable_values(df, unstable_range, unstable_threshold, 'steering')

if(apply_svagol):
    window = int(config.load_config('config.ini', 'SVAGOLFILTER', 'windowsize'))
    order = int(config.load_config('config.ini', 'SVAGOLFILTER', 'polyorder'))
    df = pop.savgol_smoothing(df, 'steering', window, order)

if(apply_exponential):
    alpha = float(config.load_config('config.ini', 'EXPONENTIALSMOOTHING', 'alpha'))
    df = pop.exponential_smoothing(df,'steering', 0.9)

if(apply_average):
    df = pop.moving_averge_with_dynamic_window(df,'steering')

if(apply_unstable):
    df = pop.replace_unstable_values(df, 'steering')


mapping_values = np.array(x)

if(apply_mapping):
    df = pop.map_to_closest_value(df, 'steering', mapping_values)


if(save_df):
    pp.save_dataframe_to_csv(df, 'data/preprocces/preprocces_data')






#calculate coordinates
df = cco.add_radius_alpha_radian_to_df(df, f, ODOMETER_TO_MM_FACTOR)


if(save_df):
    pp.save_dataframe_to_csv(df,'data/postcalc/calculatet_data')




#post proccesing
    
min_Radius = float(config.load_config('config.ini', 'POSTPROCESSINGGENERAL', 'min_radius'))

df = pop.map_low_radius_to_0(df, min_Radius)




if(save_df):
    pp.save_dataframe_to_csv(df, 'data/postprocces/postprocces_data')



my_plt.plot_graph_with_semi_circle(df)

my_plt.save_plot('data/plot/plot_'+misc.get_timestamp()+'.png')




eval = config.load_config_bool('config.ini', 'DEVELOPMENT', 'evaluate')

if eval:
    #Evaluate
    print("Abstand erster und letzter Punkt: ", ev.calculate_distance_first_last_point()) 

    #Load df for comparrison
    path_test = config.load_config('config.ini', 'DEVELOPMENT', 'compare_df_path')

    df_test = pp.read_csv_file(path_test)
    df_compare, average, standard_deviation, median, max, total = ev.evaluate_radius_diff_over_distance(df, df_test)
    print("Average: ", average)
    print("Standard deviation: ", standard_deviation)
    print("Median: ", median)
    print("Max: ", max)
    print("Total: ", total)

    if(save_df):
        pp.save_dataframe_to_csv(df_compare,'data/evaluate/evaluate_data')

df = pop.summarize_curves(df)

if(save_df):
    pp.save_dataframe_to_csv(df, 'data/graph_summery/summery_data')

#plot


my_plt.show_plot()






