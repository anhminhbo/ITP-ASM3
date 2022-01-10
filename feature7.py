# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date:
# Last modified date:
import random


def feature_7():
    """
    :return: a random voucher
    """
    rand = random.randint(0, 3)
    series = str(random.randint(100000, 999999))
    if rand == 0:
        return "DIS10-" + series
    elif rand == 1:
        return "DIS20-" + series
    elif rand == 2:
        return "DIS50-" + series


def voucher_discount(vou):
    """
    :param vou: voucher
    :return: the discount value of that voucher
    """
    return int(vou[3:5]) / 100
