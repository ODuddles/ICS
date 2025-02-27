""""
Owen Duddles 15099261
Narek Wartanian 14787148
This file has the functions to handle different strategy operations like
merging two strategies or mutating strategies. As well as going from
integer representation to list representation.
"""
import numpy as np
import json
np.random.seed(232005)

def decimal_to_base_k(n:int, k:int):
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

def base_k_to_integer(array:list, k:int):
    """ Converts a given array representing a number in base k,
    back to a decimal number given a base k"""
    ans = 0
    power = 0
    array = array[::-1]
    for num in array:
        ans += num * np.power(k, power)
        power += 1
    return int(ans)

def integer_2_binary(num:int, supposed_len:int):
    """returns the num as a binary array with length supposed_len"""
    ruletable_arr = decimal_to_base_k(num, 2)
    if len(ruletable_arr) > supposed_len:
        print("It seems the given strategy 1 integer number is too large")
        exit()
    elif len(ruletable_arr) < supposed_len:
        ruletable_arr = [0] * (supposed_len - len(ruletable_arr)) + \
                        ruletable_arr
    return ruletable_arr

def mutate(strat:int):
    """This function adjusts a strategy strat by going to the binary form of
    the strategy and changing a few 0's to 1's and 1's to 0's. How many of
    these changes are made, is determined by the parameters.json file in the
    parameters directory."""
    list_form = integer_2_binary(strat, 21)

    with open('./parameters/parameters.json', 'r') as file:
        data = json.load(file)

    nr_mutations = data["mutation_factor"]

    index_arr = np.random.choice(len(list_form), nr_mutations, replace=False)
    for i in index_arr:
        list_form[i] = (list_form[i] + 1) % 2
    return base_k_to_integer(list_form, 2)
