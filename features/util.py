def is_valid_op(fn, *args):
    """

    :param fn:
    :return:
    """
    is_valid_operation = False
    user_choice = input('Do you want to try again?(y/n): ')
    while not is_valid_operation:
        if user_choice == 'y':
            is_valid_operation = True
            if len(args) == 1:
                fn(args[0])
            elif len(args) == 2:
                fn(args[0], args[1])
            elif len(args) == 3:
                fn(args[0], args[1], args[2])

        elif user_choice == 'n':
            is_valid_operation = True
            print("Processing...")
        else:
            user_choice = input('Invalid operation, please input "y" to try again or "n" to back to the main shop: ')
