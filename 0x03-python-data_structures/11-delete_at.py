#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    # get the length of my_list
    length = len(my_list)

    # check idx, if negative or out range, return my_list as it is
    if idx < 0 or idx > (length - 1):
        return my_list

    # create new_list equal to my_list
    new_list = my_list[:]

    # loop in the indexed length
    for i in range(length):

        # when in at my_list[idx], delete it in both lists
        if i == idx:
            del my_list[i]
            del new_list[i]

    # return the new_list
    return new_list
