""""
Owen Duddles 15099261
Narek Wartanian
This file has the functions to handle a battle between 2 strategies.
"""
import json
import strategies.strategy_handling as strats

def get_index(data):
    """Based on the data tuple the according index in the strategy list is
    returned to determine the next move"""
    sec_prev_1, prev_1, sec_prev_2, prev_2 = data
    string = f"{sec_prev_1}{prev_1}{sec_prev_2}{prev_2}"

    # To indicate the end of the normal options and the start of the actions
    # when the game just starts
    n = 16
    if string == "----":
        return n
    elif "-" in string:
        return n + 1 + int(string[3]) + 2 * int(string[1])

    return int(string[3]) + 2 * int(string[2]) + 4 * int(string[1]) \
           + 8* int(string[0])

def calculate_payoff(move1, move2, payoff_dict):
    """Calculates the payoff for each strat by comparing their moves and
    looking the payoff for them in the payoff dictionary"""
    if not (move1 in [0, 1] and move2 in [0, 1]):
        print("You seem to be using invalid moves:")
        print("Move1:", move1)
        print("Move2:", move2)

    string = f"{move1}{move2}"
    return payoff_dict[string][0], payoff_dict[string][1]

def battle(strategy1, strategy2, rounds, verbose=False):
    """This function executes the battle between strategy 1 and strategy 2
    and returns the payoff for both strategies after the number of rounds. """

    # Open and read the JSON file
    with open('/home/owen/Documents/Universiteit/Jaar 2/ComputationalScience/ICS/GT/parameters/parameters.json', 'r') as file:
        data = json.load(file)

    # Extracting the payoff dictionary
    payoff_dict = data["payoff"]

    # supposed length is 21, 16 for the history and 5 moves for what happends
    # at the start of the game
    supposed_n = 21

    strat1_arr = strats.decimal_to_base_k(strategy1, 2)
    if len(strat1_arr) > supposed_n:
        print("It seems the given strategy 1 integer number is too large")
        exit()
    elif len(strat1_arr) < supposed_n:
        strat1_arr = [0] * (supposed_n - len(strat1_arr)) + strat1_arr

    strat2_arr = strats.decimal_to_base_k(strategy2, 2)
    if len(strat2_arr) > supposed_n:
        print("It seems the given strategy 2 integer number is too large")
        exit()
    elif len(strat2_arr) < supposed_n:
        strat2_arr = [0] * (supposed_n - len(strat2_arr)) + strat2_arr

    sec_prev_1 = "-"
    prev_1 = "-"
    sec_prev_2 = "-"
    prev_2 = "-"

    total_payoff_1 = 0
    total_payoff_2 = 0
    for round in range(rounds):
        # determining the index based on current history for strategy 1
        # this is different from the index_2 because each stratagy is encoded
        # as Second Previous Self, Previous Self, Second Previous Other,
        # Previous Other -> move.
        index_1 = get_index((sec_prev_1, prev_1, sec_prev_2, prev_2))
        index_2 = get_index((sec_prev_2, prev_2, sec_prev_1, prev_1))

        # Determining the moves and their resulting payoffs
        move_1 = strat1_arr[index_1]
        move_2 = strat2_arr[index_2]

        payoff_1, payoff_2 = calculate_payoff(move_1, move_2, payoff_dict)

        # Adjusting the total payoffs
        total_payoff_1 += payoff_1
        total_payoff_2 += payoff_2

        # Adjusting the history
        sec_prev_1 = prev_1
        prev_1 = move_1
        sec_prev_2 = prev_2
        prev_2 = move_2
        if verbose:
            print(f"Round {round}")
            print(f"Move 1 = {move_1} and Move 2 = {move_2}")
            print(f"Current Payoff", total_payoff_1, total_payoff_2)
            print("")

    return total_payoff_1, total_payoff_2

def tournament(poule:list, strategies:list):
    """This function runs a tournament by letting each strategy in the poule
    battle against all strategies in strategies. Strategies within the
    poule don't battle each other and strategies within the strategies variable
    also don't.
    This function returns a list of tuples with payoff's from high to low and
    their according strategy in the poule (the strategies list is just to
    have a reference of the effectivity of each strategy)"""

    with open('/home/owen/Documents/Universiteit/Jaar 2/ComputationalScience/ICS/GT/parameters/parameters.json', 'r') as file:
        data = json.load(file)

    rounds = data["iterationsPerGame"]

    result = []
    for strat1 in poule:
        total_payoff = 0
        for strat2 in strategies:
            payoff_1, _ =  battle(strat1, strat2, rounds)
            total_payoff += payoff_1
        result.append((total_payoff, strat1))
    result = sorted(result, key=lambda x: x[0], reverse=True)
    return result

print(tournament([0, 2097151, 139808, 1118464, 1973772, 2088963, 699045], [0, 2097151, 139808, 1118464, 1973772, 2088963, 699045]))

