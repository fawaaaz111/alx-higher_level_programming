#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n or i < 0:
            continue
        print("{:c}".format(ord(str[i])), end='')
