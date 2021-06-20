#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Checks to validate data
"""

def check_len(dict_: dict, index: list):
    """controls which lines are shorter than index_len and fills in missing spaces with zeros
       (AIM: dictionary with equal-length lines)"""

    index_len = len(index)
    default_value = 0  # Value to be replaced in missing spaces
    for row in dict_:
        if len(dict_[row]) < index_len:
            # Add zeroes to lists shorter than the longest one
            dict_[row] = dict_[row] + [default_value for i in range(0, (index_len - len(dict_[row])))]


def check_stat_type(stat_list: list) -> bool:
    """check that all the statistics are numerical"""

    stat_input_error = False

    for stat in stat_list:
        try:
            # Tries to convert the input into float
            # (string type input containing numeric stat does not cause errors)
            float(stat)

        except ValueError:  # Trows an exception if float(stat) causes an error (non-numerical statistics)
            print('ERROR: One or more of the stats is invalid. Insert only numbers')
            stat_input_error = True  # Notification of exception (used to cause the new request for statistics)
            break  # Exits the for loop since a non-numeric statistic is not acceptable

    return stat_input_error