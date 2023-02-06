#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for ch in range(len(str)):
        if str[ch] != n:
            s += str[ch]

    return(s)
