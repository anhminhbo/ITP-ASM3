# Main program run here
import sys
import time
import feature1 as feature1
import feature3 as feature3
import feature4 as feature4
import feature5 as feature5
import feature6 as feature6

# Set up program

# Initialize shop item class


class ShopItem:
    shop_item_counter = 1

    def __init__(self, name, color, quantity=10):
        self.id = ShopItem.shop_item_counter
        self.name = name
        self.quantity = quantity
        self.color = color
        # Increment id by 1 everytime we create a new obj
        ShopItem.shop_item_counter += 1


list_shop_items = [
    ShopItem('iphone11', 'red'),
    ShopItem('iphone12', 'blue')
]


def main():
    """
    main program will be execute here
    :return: none
    """
    print("""
Welcome to our Shop
Here are your options:
    1. List all items 
    2. List all info of a specific item  --> got embedded into feature3 and feature4, PLEASE DONT USE THIS
    3. Search item by name and list all info of that specific item 
    4. Search item by item id and list all info of that specific item 
    5. List all info of a specific customer
    6. Placing orders
    7.
    8.
    9.
    10.
    11. End program
    """)

    feature_number = 0

    try:
        feature_number = int(input("Please input your number that you would like to process with: "))
    except ValueError:
        main()

    if feature_number == 1:
        feature1.feature_1(list_shop_items)
        time.sleep(5)
        main()
    # elif feature_number == 2:
    #     feature2.feature_2(list_shop_items)
    #     time.sleep(5)
    #     main()
    elif feature_number == 3:
        feature3.feature_3(list_shop_items,main)
        time.sleep(5)
        main()
    elif feature_number == 4:
        feature4.feature_4(list_shop_items,main)
        time.sleep(5)
        main()
    elif feature_number == 5:
        feature5.feature_5(feature5.customers)
        time.sleep(5)
        main()
    elif feature_number == 6:
        feature6.feature_6(list_shop_items,main, feature5.customers)
        time.sleep(5)
        main()
    # elif feature_number == 7:
    #     feature_7(list_shop_items)
    #     time.sleep(5)
    #     main()
    # elif feature_number == 8:
    #     feature_8(list_shop_items)
    #     time.sleep(5)
    #     main()
    # elif feature_number == 9:
    #     feature_9(list_shop_items)
    #     time.sleep(5)
    #     main()
    # elif feature_number == 10:
    #     feature_10(list_shop_items)
    #     time.sleep(5)
    #     main()
    elif feature_number == 11:
        sys.exit()
    else:
        main()


if __name__ == "__main__":
    main()
