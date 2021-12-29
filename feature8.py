import random


def restock_counter():
    restock = random.randint(1, 20)
    print("Days till restock: " + str(restock))
