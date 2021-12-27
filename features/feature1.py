def feature_1(arr):
    """

    :return:
    """
    item_names = [item.name for item in arr]
    item_ids = [item.id for item in arr]

    print('List of all items in the shop: ')

    for index in range(len(item_names)):
        print(f'{item_ids[index]}. {item_names[index]}')