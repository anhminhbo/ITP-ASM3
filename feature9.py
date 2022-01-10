# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date:
# Last modified date:

# Discount -> 1 property for Customer , 3=> 10%
import util
import feature5 as f5

def membership_discount(accumulated_money, total_price=0):
    """
    This function created to upgrade the customer's membership and discount
    :param total_price: the order value
    :param accumulated_money: total amount of money the customer purchased
    :return: the discount amount
    """
    total_value = accumulated_money + total_price

    # Platinum member
    if accumulated_money >= 100000000:
        print("Platinum member. Discount: 15%")
        price = 0.15
    elif total_price >= 100000000:
        print("Congratulations, you have been promoted to platinum member!")
        price = 0.15
    elif total_value >= 100000000:
        print("Congratulations, you have been promoted to platinum member!")
        price = 0.15

    # Gold member
    elif accumulated_money >= 70000000:
        print("Gold member. Discount: 10%")
        price = 0.1
    elif total_price >= 70000000:
        print("Congratulations, you have been promoted to gold member!")
        price = 0.1
    elif total_value >= 70000000:
        print("Congratulations, you have been promoted to gold member!")
        price = 0.1

    # Silver member
    elif accumulated_money >= 30000000:
        print("Silver member. Discount: 5%")
        price = 0.05
    elif total_price >= 30000000:
        print("Congratulations, you have been promoted to silver member!")
        price = 0.05
    elif total_value >= 30000000:
        print("Congratulations, you have been promoted to silver member!")
        price = 0.05

    # Normal customer
    else:
        price = 0

    return total_price * price

def input_cust_id():
    cust_id = "A"
    while not util.is_numbers(cust_id):
        cust_id = input("Input your customer id: ")
        if not util.is_numbers(cust_id):
            print("Your input is invalid. Please input again.")
        else:
            break
    return int(cust_id)

def feature_9():
    cus_id = 10
    while cus_id > f5.Customer.customer_counter:
        cus_id = input_cust_id()
        if cus_id > f5.Customer.customer_counter:
            print(f"Cannot find the customer with the id {cus_id}. Please input again.")
        else:
            break
    cust_data = open("customer.txt", "r")
    lines = cust_data.readlines()
    cust_data.close()
    pro = lines[cus_id - 1].split(" | ")
    membership_discount(int(pro[4]))
