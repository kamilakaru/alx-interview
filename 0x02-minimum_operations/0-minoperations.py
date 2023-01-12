#!/usr/bin/python3

"""
method that determines the numbe rof minimum operations given n character
"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    args: n: nunber of charcter to be deployed
    return:
            number of min operation
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
