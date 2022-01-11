def read_info(db_schema):
    """
    This function read info from according dbSchema text file
    :param db_schema: name of text file
    :return: list of each line in the text file
    """
    # Read new info in according database
    db = open(db_schema, "r")
    lines = db.readlines()
    db.close()

    return lines


def write_info(db_schema, lines):
    """
    This function stores info into according dbSchema text file
    :param db_schema: name of text file
    :param lines: list of each line in the text file
    :return: none
    """

    # Add db into database
    db = open(db_schema, "w")
    db.writelines(lines)
    db.close()


def delete_info(db_schema, data, lines):
    """
    This function deletes info from dbSchema text file
    :param db_schema: name of text file
    :param data: data need to be deleted in the text file
    :param lines: list of each line in the text file
    :return: False if cannot delete or True if can delete
    """

    data_is_existed = False

    # Checking if the input voucher is stored and remove the used voucher
    for index in range(len(lines) - 1):
        if data + '\n' == lines[index]:
            lines.pop(index)
            data_is_existed = True
            break

    # Update database
    write_info(db_schema, lines)

    return data_is_existed
