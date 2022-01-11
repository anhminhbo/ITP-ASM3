import time


def is_numbers(string):
    return all(char.isdigit() for char in string)


def is_letters(string):
    return any(char.isalpha() for char in string)


def is_valid_op(fn, main_func, *args):
    """
    :param main_func:
    :param fn:
    :return:
    """
    is_valid_operation = False
    user_choice = input('Do you want to try again (Y/N)? ')
    while not is_valid_operation:
        if user_choice == 'y' or user_choice == 'Y':
            is_valid_operation = True
            if len(args) == 1:
                fn(args[0], main_func)
            elif len(args) == 2:
                fn(args[0], main_func, args[1])
            elif len(args) == 3:
                fn(args[0], main_func, args[1], args[2])
            elif len(args) == 0:
                fn()

        elif user_choice == 'n' or user_choice == 'N':
            is_valid_operation = True
            print("Processing...")
            time.sleep(5)
            main_func()
        else:
            user_choice = input('Invalid operation, please input "Y" to try again or "N" to back to the main shop: ')


def checkInt(text):
    """
    This function to check if a text can be converted to int
    :param text: input text to checked
    :return: True if it does not throw error when converted to int and vice versa
    """
    if text[0] in ('-', '+'):
        return text[1:].isdigit()
    return text.isdigit()
