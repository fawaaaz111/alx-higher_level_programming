#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    # check if my_list is emyty or null
    length = len(my_list)
    if length == 0 or not my_list:
        return None

    # create new list, size equal to my_list
    new_list = my_list[:]

    # loop through indexd legth
    for i in range(length):

        # if item % 2 = 0, then assign true in the new list, else false
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False

    # return the new list
    return new_list
