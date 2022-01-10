# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date:
# Last modified date:

from feature2 import feature_2
from util import is_valid_op


def feature_4(arr,main_func):
    """
    This function created to search item by name and show the information of the item
    :param arr: input list of items
    :param main_func: main function of the program
    :return: none
    """
    try:
        user_input_id = int(input("Please input the item's id: "))

        item_founded = False

        for item_obj in arr:
            if item_obj.id == user_input_id:
                item_founded = True
                feature_2(arr, item_obj)

        if not item_founded:
            print(f'Can not find this item with id of {user_input_id}.')
            is_valid_op(feature_4,main_func, arr)

    except ValueError:
        print('Invalid id.')
        is_valid_op(feature_4,main_func, arr)
