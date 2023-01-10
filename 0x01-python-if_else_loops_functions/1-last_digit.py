#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    new_number = number % 10
else:
    new_number = number % -10
print("Last digit of {} is {} and is".format(number, new_number), end='')
if new_number > 5:
    print(" greater than 5")
elif new_number == 0:
    print(" 0")
elif new_number < 6 and new_number != 0:
    print(" less than 6 and not 0")
