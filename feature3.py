# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date:
# Last modified date:

from feature2 import feature_2
from util import is_valid_op


def feature_3(arr, main_func):
    """
    Search item by name and show the info of the item
    :param arr: input list of items
    :param main_func: main function of the program
    :return: none
    """
    user_input_name = input("Please input the item's name: ")
    item_founded = False

    for item_obj in arr:
        if item_obj.name == user_input_name:
            item_founded = True
            feature_2(arr, item_obj)

    if not item_founded:
        print(f'Can not find this item with name of {user_input_name}.')

        is_valid_op(feature_3,main_func, arr)
