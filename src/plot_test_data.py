import pandas as pd
import plot as my_plt
import user_interface as ui
import matplotlib.pyplot as plt

path = ui.user_select_file()
df = pd.read_csv(path)
my_plt.plot_graph_with_semi_circle(df)

plt.xlim(0, 10)
plt.ylim(0, 10)

my_plt.show_plot()