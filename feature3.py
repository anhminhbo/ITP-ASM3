# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Nguyen Khuong (s3924577)
# Created date: 01/01/2022
# Last modified date: 05/01/2022

from feature2 import feature_2
from util import is_valid_op


def feature_3(arr, main_func):
    """
    This function created to search item by name and show the information of the item
    :param arr: input list of items
    :param main_func: main function of the program
    :return: none
    """
    # Input user search
    user_input_name = input("Please input the item's name: ")
    item_founded = False

    list_of_item = []

    # Loop through every item and append to the list with similar name to what user input
    for item_obj in arr:
        if user_input_name in item_obj.name:
            item_founded = True
            list_of_item.append(item_obj)

    # If the item is not found => Tell user that can not find the item
    if not item_founded:
        print(f'Cannot find the item with the search: {user_input_name}.')
        is_valid_op(feature_3, main_func, arr)

    # If the item is found => Print out list items
    else:
        feature_2(arr, None, list_of_item)
