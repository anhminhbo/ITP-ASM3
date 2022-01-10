# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date:
# Last modified date:
import random
import re


regex = "DIS..-......"


def is_valid_voucher(voucher):
    is_match_form = re.fullmatch(regex, voucher)
    is_stored = False
    if not is_match_form:
        return ["Your input is invalid. Please input again.", False]

    # Read database
    vou_data = open("voucher.txt", "r")
    vouchers = vou_data.readlines()
    vou_data.close()

    # Checking if the input voucher is stored
    for index in range(len(vouchers)-1):
        if voucher + '\n' == vouchers[index]:
            vouchers.pop(index)
            is_stored = True
            break

    # Update database
    vou_data = open("voucher.txt", "w")
    vou_data.writelines(vouchers)
    vou_data.close()

    if not is_stored:
        return ["This voucher is not exist. Please input another voucher.", False]

    return [True, True]


def feature_7():
    """
    :return: a random voucher
    """
    rand = random.randint(0, 3)
    series = str(random.randint(100000, 999999))
    vou = ""
    if rand == 0:
        vou = "DIS10-" + series
    elif rand == 1:
        vou = "DIS20-" + series
    elif rand == 2:
        vou = "DIS50-" + series
    vou += "\n"
    # Store generated voucher in database
    vou_data = open("voucher.txt", "r")
    vouchers = vou_data.readlines()
    vou_data.close()

    vouchers.append(vou)
    vou_data = open("voucher.txt", "w")
    vou_data.writelines(vouchers)
    vou_data.close()

    return vou


def voucher_discount(vou):
    """
    :param vou: voucher
    :return: the discount value of that voucher
    """
    return int(vou[3:5]) / 100
