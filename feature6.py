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
from util import is_valid_op, checkInt


class ShopItem:
    shop_item_counter = 1

    def __init__(self, name, color, price=0, quantity=10):
        self.id = ShopItem.shop_item_counter
        self.name = name
        self.quantity = quantity
        self.color = color
        self.price = price
        # Increment id by 1 everytime we create a new obj
        ShopItem.shop_item_counter += 1


list_shop_items = [
    ShopItem('iphone11', 'red', 10000000),
    ShopItem('iphone12', 'blue', 7000000)
]


def feature_6(arr, main_func, cus_list):
    """
    This function created to fill and show the placing orders of the customer
    :param main_func:
    :param cus_list: input list of customers
    :param arr: input list of items
    :return: none
    """
    item_existed = False

    try:
        pro_id = int(input("Please input the item's id: "))
        buy_qtt = int(input("Please input your desired quantity: "))
        print("Checking for availability of product...")
        time.sleep(1)
        for item_obj in arr:
            if item_obj.id == pro_id:
                item_existed = True
                if buy_qtt > item_obj.quantity:
                    print(f'The quantity of goods is not enough, only {item_obj.quantity} left.')
                    is_valid_op(feature_6, main_func, arr, cus_list)
                else:
                    def input_cust_id():
                        cust_existed = False
                        cust_id = input("The number of your desired product is sufficient."
                                        " Please input your customer id: ")
                        is_cust_id_int = checkInt(cust_id)
                        if is_cust_id_int:
                            for cus_obj in cus_list:
                                if cus_obj.id == int(cust_id):
                                    cust_existed = True
                                    total_price = int(item_obj.price * buy_qtt)

                                    # Update accumulated money in database
                                    cust_data = open("customer.txt", "r")
                                    lines = cust_data.readlines()
                                    cust_data.close()
                                    pro = lines[cus_obj.id - 1].split(" | ")

                                    # Checking the condition to upgrade membership
                                    dis_amount = feature9.membership_discount(int(pro[4]), total_price)
                                    total_price -= dis_amount

                                    # Voucher discount
                                    check_vou = input("Do you want to use a voucher (Y/N)? ")
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

                                    cust_data = open("customer.txt", "w")
                                    cust_data.writelines(lines)
                                    cust_data.close()
                                    feature5.customers = feature5.refresh_customer_data()

                            if not cust_existed:
                                print(f'your customer id of {cust_id} does not exist.')
                                is_valid_op(input_cust_id, main_func)
                        else:
                            print('Invalid customer id.')
                            is_valid_op(input_cust_id, main_func)

                    input_cust_id()
                    break

        if not item_existed:
            print(f'This item with id of {pro_id} not exist in the shop.')
            is_valid_op(feature_6, main_func, arr, cus_list)

    except ValueError:
        print('Item id or desired quantity is invalid.')
        is_valid_op(feature_6, main_func, arr, cus_list)
