""""
Owen Duddles
Narek Wartanian
This file has the functions to handle different strategy operations like
merging two strategies or mutating strategies. As well as going from
integer representation to list representation.
"""
import numpy as np

def decimal_to_base_k(n, k):
    """Converts a given decimal (i.e. base-10 integer) to a list containing the
    base-k equivalant.

    For example, for n=34 and k=3 this function should return [1, 0, 2, 1]."""

    results = []

    while n > 0:
        rem = n % k
        results.insert(0, int(rem))
        n -= rem
        n /= k

    return results


def base_k_to_integer(array, k):
    """ Converts a given array representing a number in base k,
    back to a decimal number given a base k"""
    ans = 0
    power = 0
    array = array[::-1]
    for num in array:
        ans += num * np.power(k, power)
        power += 1
    return int(ans)
