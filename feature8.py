import random
import time


def restock_condition(list_obj):
    """

    :param list_obj:
    :return:
    """
    goods = int(input("Quantities of goods: "))
    for obj in list_obj:
        if obj.quantity == 0:
            time_needed = random.randint(10,30)
            restock_counter(time_needed)
            obj.quantity += goods


def restock_counter(t):
    """

    :param t:
    :return:
    """
    while not t == -1:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Time remaining until restocked: ', timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Finish restocking")
