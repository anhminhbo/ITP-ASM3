# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh (s3931605) and Vu Quoc Gia Quan (s3927120)
# Created date:
# Last modified date:

def take_id():
    return Customer.customer_counter


def reset_id():
    Customer.customer_counter = 0


class Customer:
    customer_counter = 0

    def __init__(self, name, email_address, shipping_address, phone_number, accumulated_amount=0):
        Customer.customer_counter += 1
        self.id = Customer.customer_counter
        string_lst = name.split(" ")
        self.first_name = string_lst[0]
        self.last_name = string_lst[1]
        self.email_address = email_address
        self.shipping_address = shipping_address
        self.phone_number = phone_number
        self.accumulated_amount = accumulated_amount

    def show_customer_info(self):
        print(f"""
        Customer id: {self.id}
        Name: {self.first_name + ' ' + self.last_name}
        Email address: {self.email_address}
        Shipping address: {self.shipping_address}
        Phone number: {self.phone_number}
        Accumulated amount of spent money: {self.accumulated_amount}""")


def refresh_customer_data():
    """
    This function created to refresh the customer's data
    :return: customer data
    """
    cust = []
    reset_id()
    cus_data = open("customer.txt", "r")
    lines = cus_data.readlines()
    for line in lines:
        # read properties
        pro = line.split(" | ")
        cust.append(Customer(pro[0], pro[1], pro[2], pro[3], int(pro[4])))
    cus_data.close()
    return cust


def feature_5(customer_list):
    """
    This function created to show the customer's information
    :param customer_list:
    :return:
    """
    for customer in customer_list:
        customer.show_customer_info()


customers = refresh_customer_data()


