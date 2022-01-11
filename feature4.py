# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date: 04/01/2022
# Last modified date: 06/01/2022

from feature2 import feature_2
from util import is_valid_op


def feature_4(arr, main_func):
    """
    This function created to search item by name and show the information of the item
    :param arr: input list of items
    :param main_func: main function of the program
    :return: none
    """
    # Handle error if user input a text not a number
    try:
        user_input_id = int(input("Please input the item's id: "))

        item_founded = False

        # If the id match the id of the item => Print out the item info
        for item_obj in arr:
            if item_obj.id == user_input_id:
                item_founded = True
                feature_2(arr, item_obj, [])

        # If not match => Tell user can not find item
        if not item_founded:
            print(f'Cannot find the item with the id {user_input_id}.')
            is_valid_op(feature_4, main_func, arr)

    # When user input wrong format => rerun the function
    except ValueError:
        print('Invalid id.')
        is_valid_op(feature_4, main_func, arr)
