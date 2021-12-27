# Main program run here
import sys
import time
import features.feature1 as feature1

# Set up program
class shop_item():
    shop_item_counter = 1

    def __init__(self, name, color, quantity=10):
        self.name = name
        self.id = shop_item.shop_item_counter
        self.quantity = quantity
        self.color = color
        shop_item.shop_item_counter += 1

    def show_value(self):
        print('id of item:', self.id)
        print('name of item:', self.name)
        print('color of item:', self.color)
        print('quantity of item:', self.quantity)


list_items = [
    shop_item('iphone11', 'red'),
    shop_item('iphone12', 'blue')
]

# print(list_items[0].__dict__)

def main():
    """

    :return:
    """


    print("""
    Welcome to our Shop
    Here are your options:
        1. List all items 
        2. List all info of a specific item 
        3. Search item by name 
        4. Search item by item id 
        5. List all info of a specific customer
        6. Placing orders


        11. End program
    """)

    try:
        feature_number = int(input("Please input your number that you would like to process with: "))
    except Exception:
        main()

    if feature_number == 1:
        feature1.feature_1(list_items)
        time.sleep(5)
        main()
    # elif feature_number == 2:
    #     feature_2(list_items)
    # elif feature_number == 3:
    #     feature_3(list_items)
    # elif feature_number == 4:
    #     feature_4(list_items)
    # elif feature_number == 5:
    #     feature_5(list_items)
    # elif feature_number == 6:
    #     feature_6(list_items)
    # elif feature_number == 7:
    #     feature_7(list_items)
    # elif feature_number == 8:
    #     feature_8(list_items)
    # elif feature_number == 9:
    #     feature_9(list_items)
    # elif feature_number == 10:
    #     feature_10(list_items)
    elif feature_number == 11:
        sys.exit()
    else:
        main()

main()