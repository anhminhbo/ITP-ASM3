# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Vu Quoc Gia Quan (s3927120)
# Created date:
# Last modified date:

from texttable import Texttable


def feature_2(arr, item_obj, list_obj):
    """
    This function created to show specific item information
    :param arr: input list of items
    :param item_obj: input item object from the shop items for feature 2
    :param list_obj: input list of item from feature 3
    :return: none
    """
    # Feature 3
    if len(list_obj) != 0:
        # Create a table to format print out
        table = Texttable()

        # Access __dict__ property of class to get a dict of all keys and output
        # necessary keys, here is id and name
        category_list = list(arr[0].__dict__.keys())

        print('Info of the item with your search: ')

        # Initialize names for the header and the row values of the item
        table_list = [category_list]

        for item in list_obj:
            table_list.append(list(item.__dict__.values()))

        # Add each row inside table and print it out
        table.add_rows(table_list)
        table.set_cols_dtype(["a", "a", "a", "a", "i"])
        table.set_cols_width([2, 20, 10, 20, 10])

        print(table.draw())

    else:
        # Feature 4
        # Create a table to format print out
        table = Texttable()

        # Access __dict__ property of class to get a dict of all keys and output
        # necessary keys, here is id and name
        category_list = list(arr[0].__dict__.keys())

        print('Info of the item with your search: ')

        # Initialize names for the header and the row values of the item
        table_list = [category_list, list(item_obj.__dict__.values())]

        # Add each row inside table and print it out
        table.add_rows(table_list)
        table.set_cols_dtype(["a", "a", "a", "a", "i"])
        table.set_cols_width([2, 20, 10, 20, 10])

        print(table.draw())
