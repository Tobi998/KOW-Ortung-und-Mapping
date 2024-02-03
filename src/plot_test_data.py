"""
This file is used to plot prepared data and has no greater relevance to the project.
"""

import pandas as pd
import plot as my_plt
import user_interface as ui

path = ui.user_select_file()
df = pd.read_csv(path)
my_plt.plot_graph_with_semi_circle(df)



my_plt.show_plot()