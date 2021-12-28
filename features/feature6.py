import time
from .util import is_valid_op


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


def feature_6(arr, cus_list):
    """
    :param cus_list: input list of customers
    :param arr: input list of items
    :return: none
    """
    item_existed = False

    cust_existed = False

    try:
        pro_id = int(input("Please input the item's id: "))
        buy_qtt = int(input("Please input your desired quantity: "))
        print("Checking for availability of product...")
        time.sleep(1)
        for item_obj in arr:
            if item_obj.id == pro_id:
                item_existed = True
                if buy_qtt > item_obj.quantity:
                    print(f'The quantity of goods is not enough, only {item_obj.quantity} left.')
                    is_valid_op(feature_6, arr, cus_list)
                else:
                    while True:
                        try:
                            cus_id = int(input("The number of your desired product is sufficient."
                                               " Please input your customer id: "))
                            break
                        except ValueError:
                            print('Invalid customer id.')

                    item_obj.quantity -= buy_qtt
                    for cus_obj in cus_list:
                        if cus_obj.id == cus_id:
                            cust_existed = True
                            print(f"{cus_obj.name}'s order is successfully done.")
                    if not cust_existed:
                        print(f'your customer id of {cus_id} does not exist.')
                        is_valid_op(feature_6, arr, cus_list)
                    break

        if not item_existed:
            print(f'this item with id of {pro_id} not exist in the shop.')
            is_valid_op(feature_6, arr, cus_list)
    except ValueError:
        print('item id or desired quantity is invalid.')
        is_valid_op(feature_6, arr, cus_list)
