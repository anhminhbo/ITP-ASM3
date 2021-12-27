from .feature2 import feature_2


def feature_3(arr):
    """
    Search item by name and show the info of the item
    :param arr: input list of items
    :return: none
    """
    user_input_name = input("Please input the item's name: ")
    item_founded = False

    for item_obj in arr:
        if item_obj.name == user_input_name:
            item_founded = True
            feature_2(arr, item_obj)

    if not item_founded:
        print('Can not find this item, please try again later.')
