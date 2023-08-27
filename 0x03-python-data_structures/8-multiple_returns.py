#!/usr/bin/python3
def multiple_returns(sentence):

    length = len(sentence)
    if len == 0 or not sentence:
        first = None
    else:
        first = sentence[0]

    the_tuple = (length, first)
    return the_tuple
