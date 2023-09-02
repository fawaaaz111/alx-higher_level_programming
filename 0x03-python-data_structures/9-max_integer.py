#!/usr/bin/python3
def max_integer(my_list=[]):

    # find the length, if emty return None
    length = len(my_list)
    if length == 0 or not my_list:
        return None

    # assume max value at index my_list[0]
    max_value = my_list[0]

    # iterate through each value make comparison and update max value
    for i in range(length):
        if my_list[i] > max_value:
            max_value = my_list[i]

    # return the max
    return max_value
