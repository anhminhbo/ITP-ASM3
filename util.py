# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date: 04/01/2022
# Last modified date: 06/01/2022

import time


def is_yes_or_no(temp):
    return temp == "Y" or temp == "y" or temp == "N" or temp == "n"


# Check if the string contains numbers
def is_numbers(string):
    """
    This function check if the text is all numbers or not
    :param string: input string
    :return: Boolean
    """
    return all(char.isdigit() for char in string)


# Check if the string contains letters
def is_letters(string):
    """
    This function check if the text is all letters or not
    :param string: input string
    :return: Boolean
    """
    return any(char.isalpha() for char in string)


# To rerun the function if the user input Yes and back to the main shop if No
def is_valid_op(fn, main_func, *args):
    """
    This function will rerun the function if the user Yes or No to back to main program
    :param main_func: main function of the program
    :param fn: the function that need to be rerun
    :return: none
    """

    is_valid_operation = False
    user_choice = input('Do you want to try again (Y/N)? ')
    # Check the user input and number of argument with each rerun function
    while not is_valid_operation:
        if user_choice == 'y' or user_choice == 'Y':
            is_valid_operation = True
            if len(args) == 1:
                fn(args[0], main_func)
            elif len(args) == 2:
                fn(args[0], main_func, args[1])
            elif len(args) == 3:
                fn(args[0], main_func, args[1], args[2])
            elif len(args) == 0:
                fn()

        # If no back to main program
        elif user_choice == 'n' or user_choice == 'N':
            is_valid_operation = True
            print("Processing...")
            time.sleep(5)
            main_func()

        # If user input wrong rerun the input yes or no
        else:
            user_choice = input('Invalid operation, please input "Y" to try again or "N" to back to the main shop: ')
