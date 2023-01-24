#!/usr/bin/python3
for num in range(0, 100): #number
    # get the first and second part of a number
    first, second = num / 10, num % 10
    if num != 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num))
