# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: SGS_Group11_3
# Created date:
# Last modified date:

# Main program run here
import sys
import time
import feature1 as feature1
import feature3 as feature3
import feature4 as feature4
import feature5 as feature5
import feature6 as feature6
import feature7 as feature7
import feature8 as feature8
import feature9 as feature9
import feature10 as feature10


# Set up program

# Initialize shop item class


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
    ShopItem('Iphone 11', 'Red', 11900000),
    ShopItem('Iphone 12 mini', 'Blue', 15500000),
    ShopItem('Iphone 6s', 'Black', 3500000),
    ShopItem('Iphone 7', 'Black', 4500000),
    ShopItem('Iphone X', 'Silver', 8000000),
    ShopItem('Iphone 12 Pro', 'Rose Gold', 19000000),
    ShopItem('iPhone 13 Pro Max', 'Blue', 60000000),
    ShopItem('Samsung Galaxy S8', 'White', 6500000),
    ShopItem('Samsung Galaxy S21 Ultra', 'Black', 25100000),
    ShopItem('Samsung Galaxy A12', 'Black', 3600000),
    ShopItem('Samsung Galaxy Z Fold3', 'Black', 43000000),
    ShopItem('Samsung Galaxy Z Flip3', 'Rose Gold', 26000000),
    ShopItem('Oppo A15s', 'Navy Blue', 4000000),
    ShopItem('Oppo Reno5 5G', 'Silver', 10000000),
    ShopItem('Xiaomi Redmi Note 10', 'Gold', 7300000),
    ShopItem('Xiaomi 11 5G', 'Silver', 14000000),
    ShopItem('Xiaomi Redmi 9A', 'Green', 2500000),
    ShopItem('Nokia C20', 'Black', 2000000),
    ShopItem('Nokia 8.3 5G', 'Silver', 9000000),
    ShopItem('Vivo V20 SE', 'Grey', 5500000)
]


def main():
    """
    The main program will be executed here
    :return: none
    """
    print("""
Welcome to our Shop
Here are your options:
    1. List all items 
    2. List all info of a specific item  --> got embedded into feature 3 and feature 4, PLEASE DON'T USE THIS
    3. Search item by name and list all info of that specific item 
    4. Search item by item id and list all info of that specific item 
    5. List all info of a specific customer
    6. Placing orders
    7. Receive a random voucher for new customer
    8. Restock all the goods (notice if the goods is sufficient)
    9. Check membership and discount by customer id
    10. Add new member
    11. End program
    """)

    feature_number = 0

    try:
        feature_number = int(input("Please input your number that you would like to process with: "))
    except ValueError:
        main()

    if feature_number == 1:
        feature1.feature_1(list_shop_items)
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 3:
        feature3.feature_3(list_shop_items, main)
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 4:
        feature4.feature_4(list_shop_items, main)
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 5:
        feature5.feature_5(feature5.customers)
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 6:
        feature6.feature_6(list_shop_items, main, feature5.customers)
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 7:
        print(f"Your voucher is: {feature7.feature_7()}")
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 8:
        feature8.restock_condition(list_shop_items)
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 9:
        feature9.feature_9()
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 10:
        feature10.feature_10()
        print("\nYour process is done. Returning back...")
        time.sleep(5)
        main()
    elif feature_number == 11:
        sys.exit()
    else:
        main()


if __name__ == "__main__":
    main()
