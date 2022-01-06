import random
import time


def restock_condition(y):
    goods = int(input("Quantities of goods: "))
    if y.quantity == 0:
        time_needed = random.randint(30, 100)
        restock_counter(time_needed)
        y.quantity += goods


def restock_counter(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Finish restocking")
