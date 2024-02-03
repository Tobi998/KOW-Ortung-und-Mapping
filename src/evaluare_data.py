import pre_process as pp
import evaluate as ev
import user_interface as ui


path = ui.user_select_file()
df = pp.read_csv_file(path)






average, standard_deviation, median, max, total = ev.evaluate_radius_diff_from_compared_df(df)
print("Average: ", average)
print("Standard deviation: ", standard_deviation)
print("Median: ", median)
print("Max: ", max)
print("Total: ", total)