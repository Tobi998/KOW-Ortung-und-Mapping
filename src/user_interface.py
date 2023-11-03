"""
This moudule contains functions to interact with the user
"""

import tkinter as tk
from tkinter import filedialog

def user_select_file():
    """
    This function asks the user to select a file and returns the file path

    :return: The file path of the selected file
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="data", filetypes=[("CSV Files", "*.csv")])
    return file_path


#print(user_select_file())