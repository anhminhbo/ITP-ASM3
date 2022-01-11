# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Vu Quoc Gia Quan (s3927120)
# Created date:
# Last modified date:

# import needed function
import random
import time


# Define has letter function
def has_letters(string):
    """
    This function check whether a data las letter or not
    :param string:
    :return: boolean
    """
    # Return true or false depending on if the data has string or not
    return any(char.isalpha() for char in string)


# Define restock condition function
def restock_condition(list_obj):
    """
    This function created to restock the out-of-stock product
    :param list_obj: list of goods
    :return: none
    """
    # Call a empty goods variable
    goods = ""
    # Make a conditional statement to check for user input
    while has_letters(goods) or goods == "":
        goods = input("Quantity of goods to be restocked: ")
        # if the user input has letters then print out following statement and run the program again
        if has_letters(goods) or goods == "":
            print("Your input is invalid. Please input again.")
            time.sleep(0.5)
        else:
            break
    # convert the value in goods variable to integer
    goods = int(goods)
    # define a restocked variable to False boolean value
    restocked = False
    # Make a for loop to check the quantity of object in the list
    for obj in list_obj:
        # Make a conditional statement to check if the quantity of an object is 0 or not
        if obj.quantity == 0:
            # if true then redefine restock variable to true
            restocked = True
            # Make a variable to take a random integer number from 5 to 10 as seconds
            time_needed = random.randint(5, 10)
            # run restock_counter function
            restock_counter(time_needed)
            # Add the wanted goods to the quantity of object
            obj.quantity += goods
    # Make another conditional statement to check if restocked is false or not
    if not restocked:
        # if restocked is false then print out the following message
        print("The remaining goods is sufficient. No need to restock.")


# define a countdown timer function
def restock_counter(t):
    """
    This function created to show the time remaining for restocking the product
    :param t: time in sec
    :return: none
    """
    # Make a conditional statement to check when the countdown timer is still above -1
    while not t == -1:
        # Define 2 variables to make minutes and seconds in the timer
        mins, secs = divmod(t, 60)
        # Make a format for the timer
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # After each second passed the timer minus 1 and continue
        t -= 1
        # Make another conditional statement to check whether the timer has run out or not and display correctly
        if not t == -1:
            print('Time remaining until restocked: ', timer, end="\r")
        else:
            print('Time remaining until restocked: ', timer, end="\n")
        time.sleep(1)
    # Display the ending message when timer has run out
    print("Finish restocking.")
