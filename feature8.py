# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Vu Quoc Gia Quan (s3927120)
# Created date:
# Last modified date:

import random
import time


def restock_condition(y):
    goods = int(input("Quantities of goods: "))
    if y.quantity == 0:
        time_needed = random.randint(30, 100)
        restock_counter(time_needed)
        y.quantity += goods


def restock_counter(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Finish restocking")
