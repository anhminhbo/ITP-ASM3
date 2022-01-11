# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date: 28/12/2021
# Last modified date: 03/01/2022
from texttable import Texttable


def feature_1(arr):
    """
    This function created to show all the item's name in the shop
    :param arr: input list of items
    :return: none
    """
    # Use text table obj from lib to format print
    table = Texttable()

    # Access __dict__ property of class to get a dict of all keys and output
    # necessary keys, here is id and name
    category_list = list(arr[0].__dict__.keys())

    print('List of all items in the shop: ')

    # Initialize names for the header
    table_list = [category_list]

    for item_obj in arr:
        # Initialize a value list to hold all the value in one row
        values_list = []
        for v in item_obj.__dict__.values():
            values_list.append(v)
        # Append the value list inside the table_lists prepare to format
        table_list.append(values_list)

    # Each item in table_list is a row in the table
    table.add_rows(table_list)
    table.set_cols_dtype(["a", "a", "a", "a", "i"])
    table.set_cols_width([2, 20, 10, 20, 10])

    print(table.draw())
