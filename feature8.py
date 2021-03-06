# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Vu Quoc Gia Quan (s3927120)
# Created date:
# Last modified date:

import random
import time


def has_letters(string):
    return any(char.isalpha() for char in string)


def restock_condition(list_obj):
    """
    This function created to restock the out of stock product
    :param list_obj: list of goods
    :return: none
    """

    goods = ""
    while has_letters(goods) or goods == "":
        goods = input("Quantity of goods to be restocked: ")
        if has_letters(goods) or goods == "":
            print("Your input is invalid. Please input again.")
            time.sleep(0.5)
        else:
            break

    goods = int(goods)
    restocked = False
    for obj in list_obj:
        if obj.quantity == 0:
            restocked = True
            time_needed = random.randint(5, 10)
            restock_counter(time_needed)
            obj.quantity += goods
    if not restocked:
        print("The remaining goods is sufficient. No need to restock.")


def restock_counter(t):
    """
    This function created to show the time remaining for restocking the product
    :param t: time in sec
    :return: none
    """
    while not t == -1:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        t -= 1
        if not t == -1:
            print('Time remaining until restocked: ', timer, end="\r")
        else:
            print('Time remaining until restocked: ', timer, end="\n")
        time.sleep(1)
    print("Finish restocking.")
