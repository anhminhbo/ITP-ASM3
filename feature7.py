# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605)
# Created date:
# Last modified date:
import random
import re
import db

regex = "DIS..-......"


def is_valid_voucher(voucher):
    is_match_form = re.fullmatch(regex, voucher)
    if not is_match_form:
        return ["Your input is invalid. Please input again.", False]

    # Read database
    vouchers = db.read_info("voucher.txt")

    # Checking if the input voucher is stored and remove the used voucher
    is_deleted = db.delete_info("voucher.txt", voucher, vouchers)

    if not is_deleted:
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
    vouchers = db.read_info("voucher.txt")

    vouchers.append(vou)
    db.write_info("voucher.txt", vouchers)

    return vou


def voucher_discount(vou):
    """
    :param vou: voucher
    :return: the discount value of that voucher
    """
    return int(vou[3:5]) / 100
