# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Nguyen Khuong (s3924577) and Truong Hoang Tuan Kiet (s3926873)
# Created date:
# Last modified date:

import time
import feature5 as feature5
import feature7 as feature7
import feature9 as feature9
from util import is_valid_op, is_numbers, is_yes_or_no
import db


def feature_6(arr, main_func, cus_list):
    """
    This function created to fill and show the placing orders of the customer
    :param main_func:
    :param cus_list: input list of customers
    :param arr: input list of items
    :return: none
    """
    item_existed = False

    pro_id = "AAAA"
    while not is_numbers(pro_id) or pro_id == "":
        pro_id = input("Input product id: ")
        if not is_numbers(pro_id) or pro_id == "":
            print("Your input is invalid. Please input again.")
            time.sleep(0.5)
        else:
            break
    pro_id = int(pro_id)

    for item_obj in arr:
        if item_obj.id == pro_id:
            item_existed = True

            # Now ask the user for how many products the user want to buy
            buy_qtt = "AAAA"
            while not is_numbers(buy_qtt) or buy_qtt == "" or buy_qtt == "0":
                buy_qtt = input("Input your desired quantity: ")
                if not is_numbers(buy_qtt) or buy_qtt == "" or buy_qtt == "0":
                    print("Your input is invalid. Please input again.")
                    time.sleep(0.5)
                else:
                    break
            buy_qtt = int(buy_qtt)

            print("Checking for availability of product...")
            time.sleep(1)

            if buy_qtt > item_obj.quantity:
                print(f'The quantity of goods is not enough, only {item_obj.quantity} left.')
                is_valid_op(feature_6, main_func, arr, cus_list)
            else:
                def input_cust_id():
                    cust_existed = False
                    notice = "The number of your desired product is sufficient. Please input your customer id: "
                    cust_id = "AAAA"
                    while not is_numbers(cust_id) or cust_id == "":
                        cust_id = input(notice)
                        if not is_numbers(cust_id) or cust_id == "":
                            print("Your input is invalid. Please input again.")
                        else:
                            break
                    cust_id = int(cust_id)
                    for cus_obj in cus_list:
                        if cus_obj.id == int(cust_id):
                            cust_existed = True
                            total_price = int(item_obj.price * buy_qtt)

                            # Update accumulated money in database
                            lines = db.read_info("customer.txt")
                            pro = lines[cus_obj.id - 1].split(" | ")

                            # Checking the condition to upgrade membership
                            dis_amount = feature9.membership_discount(int(pro[4]), total_price)
                            total_price -= dis_amount

                            # Voucher discount
                            # NOTICE: this will discount on the price after discount of membership
                            check_vou = None
                            while not is_yes_or_no(check_vou):
                                if not is_yes_or_no(check_vou):
                                    if check_vou is not None:
                                        print("Your input is invalid. Please input again.")
                                    check_vou = input("Do you want to use a voucher (Y/N)? ")
                                else:
                                    break

                            if check_vou == "Y" or check_vou == "y":
                                temp = [True, False]
                                while not temp[1]:
                                    vou = input("Input your voucher: ")
                                    temp = feature7.is_valid_voucher(vou)
                                    if not temp[1]:
                                        print(temp[0])
                                    else:
                                        break
                                total_price -= total_price * feature7.voucher_discount(vou)

                            # Purchasing
                            total_price = int(total_price)
                            print(f"Total price: {total_price}")
                            print("Processing...")
                            time.sleep(1)
                            print(f"{cus_obj.first_name}'s order is successfully done.")
                            item_obj.quantity -= buy_qtt

                            # Checking the accumulated money to upgrade membership
                            pro[4] = str(int(pro[4]) + total_price) + "\n"
                            lines[cus_obj.id - 1] = " | ".join(pro)
                            db.write_info("customer.txt", lines)
                            feature5.customers = feature5.refresh_customer_data()

                    if not cust_existed:
                        print(f'Your customer id of {cust_id} does not exist.')
                        is_valid_op(input_cust_id, main_func)

                input_cust_id()
                break

    if not item_existed:
        print(f'The item with id {pro_id} not exist in the shop.')
        is_valid_op(feature_6, main_func, arr, cus_list)
