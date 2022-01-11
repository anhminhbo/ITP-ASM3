# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: Nguyen Cuong Anh Minh(s3927120) and Nguyen Nguyen Khuong (s3924577)
# Created date: 28/12/2021
# Last modified date: 11/01/2022

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

    # Add data into database
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
    # Checking if the input data is stored and remove the used data
    for index in range(len(lines)):
        if data + '\n' == lines[index]:
            lines.pop(index)
            data_is_existed = True
            break

    # Update database
    write_info(db_schema, lines)

    return data_is_existed
