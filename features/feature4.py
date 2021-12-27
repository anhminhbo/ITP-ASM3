from .feature2 import feature_2


def feature_4(arr):
    """
    Search item by name and show the info of the item
    :param arr: input list of items
    :return: none
    """
    user_input_id = int(input("Please input the item's id: "))
    item_founded = False

    for item_obj in arr:
        if item_obj.id == user_input_id:
            item_founded = True
            feature_2(arr, item_obj)

    if not item_founded:
        print('Can not find this item, please try again later.')
