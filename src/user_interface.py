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


def ask_user_true_false(text):
    """
    Show the user a text and ask him to answer with true or false

    :param text: The text to show the user
    """
    root = tk.Tk()
    root.withdraw()
    answer = tk.messagebox.askyesno("Question", text)
    return answer

def ask_user_for_character(text):
    """
    Show the user a text and ask him to answer with a character

    :param text: The text to show the user
    :return: The character the user entered
    """
    root = tk.Tk()
    root.withdraw()
    answer = tk.simpledialog.askstring("Input", text)
    return answer	
