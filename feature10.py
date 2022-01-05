import time
import feature5 as feature5
import re

# Make a regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for validating an Email
def is_valid_email(email):
    # pass the regular expression and the string into the fullmatch() method
    return re.fullmatch(regex, email)


def has_numbers(string):
    return any(char.isdigit() for char in string)


def has_letters(string):
    return any(char.isalpha() for char in string)


def feature_10():
    name = input("Please input your name (first name + last name): ")
    if has_numbers(name):
        print("Your input is invalid. Please input again.")
        feature_10()
        return 0
    email_add = "x"
    while not is_valid_email(email_add):
        email_add = input("Please input your email address (your_email@example.com): ")
        if not is_valid_email(email_add):
            print("Your input is invalid. Please input again.")
            time.sleep(0.5)
        else:
            break
    ship_add = input("Please input your address: ")
    ph_num = "A"
    while has_letters(ph_num):
        ph_num = input("Please input your phone number: ")
        if has_letters(ph_num):
            print("Your input is invalid. Please input again.")
            time.sleep(0.5)
        else:
            break
    feature5.customers.append(feature5.Customer(name, email_add, ship_add, ph_num))
    ch = input(f"Your information has been added. Your id is {feature5.take_id()}. Please remember your id to "
               f"place order. Do you want to check (Y/N)? ")
    if ch == "Y" or ch == "y":
        for i in feature5.customers:
            if i.id == feature5.take_id():
                i.show_customer_info()


# feature_10()


