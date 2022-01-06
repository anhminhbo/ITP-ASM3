import random
import time


def has_letters(string):
    return any(char.isalpha() for char in string)


def restock_condition(list_obj):
    """
    :param list_obj: list of goods
    :return: none
    """

    goods = "A"
    while has_letters(goods):
        goods = input("Quantity of goods: ")
        if has_letters(goods):
            print("Your input is invalid. Please input again.")
            time.sleep(0.5)
        else:
            break

    goods = int(goods)
    restocked = False
    for obj in list_obj:
        if obj.quantity == 0:
            restocked = True
            time_needed = random.randint(5, 10)
            restock_counter(time_needed)
            obj.quantity += goods
    if not restocked:
        print("The remaining goods is sufficient. No need to restock.")


def restock_counter(t):
    """
    :param t: time in sec
    :return: none
    """
    while not t == -1:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        t -= 1
        if not t == -1:
            print('Time remaining until restocked: ', timer, end="\r")
        else:
            print('Time remaining until restocked: ', timer, end="\n")
        time.sleep(1)
    print("Finish restocking.")
