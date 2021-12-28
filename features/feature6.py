import features.feature5 as feature5
import time

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


def feature6(arr, cus_list):
    """
    :param cus_list: input list of customers
    :param arr: input list of items
    :return: none
    """
    Pro_id = int(input("Please input the item's id: "))
    Buy_qtt = int(input("Please input your desired quantity: "))
    print("Checking for availability of product...")
    time.sleep(1)
    for item_obj in arr:
        if item_obj.id == Pro_id:
            if Buy_qtt > item_obj.quantity:
                print("The quantity of goods is not enough. Please try again.")
                feature6(arr)
            else:
                item_obj.quantity -= Buy_qtt
                Cus_id = int(input("The number of your desired product is sufficient. Please input your customer id: "))
                for cus_obj in cus_list:
                    if cus_obj.id == Cus_id:
                        print(f"{cus_obj.name}'s order is successfully done.")
                break


feature6(list_shop_items, feature5.customers)

