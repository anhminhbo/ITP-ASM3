import random
import time


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
    ShopItem('iphone12', 'blue'),
    ShopItem('iphone6s', 'black'),
    ShopItem('iphone7', 'black'),
    ShopItem('Gao phone', 'killer red limited edition'),
    ShopItem('Orga driver', 'black on gold'),
    ShopItem('Gao phone', 'victory gold'),
    ShopItem('Samsung Galaxy S21 Ultra', 'black', 45000000),
    ShopItem('iPhone 13 Pro Max', 'blue', 67000000),
    ShopItem('Samsung Galaxy S21 Plus', 'black', 75000000),
    ShopItem('Nokia rock-smasher 1100', 'black', 999999999999),
    ShopItem('iPhone 6 Falcon Supernova Pink Diamond', 'gold', 123456789987654321),

]


def restock_condition():
    time_needed = random.randint(30, 100)
    restock_counter(time_needed)


def restock_counter(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Finish restocking")


if ShopItem.quantity() == 0:
    restock_condition()
