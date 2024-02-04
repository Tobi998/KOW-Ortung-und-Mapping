"""
This file contains miscellaneous functions that are used in the project.
"""

import datetime
def get_timestamp():
    """
    This function returns the current time as a string

    :return: The current time as a string
    """
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")
    return timestamp

