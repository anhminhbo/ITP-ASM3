# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date:
# Last modified date:

from texttable import Texttable


def feature_2(arr, item_obj):
    """
    show specific item info
    :param arr: input list of items
    :param item_obj: input item object from the shop items
    :return: none
    """
    # Create a table to format print out
    table = Texttable()

    # Access __dict__ property of class to get a dict of all keys and output
    # necessary keys, here is id and name
    category_list = list(arr[0].__dict__.keys())

    print('Info of the item: ')

    # Initialize names for the header and the row values of the item
    table_list = [category_list, list(item_obj.__dict__.values())]

    # Add each row inside table and print it out
    table.add_rows(table_list)

    print(table.draw())
