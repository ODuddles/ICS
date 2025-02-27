""""
Owen Duddles 15099261
Narek Wartanian 14787148
This file has the functions to handle a battle between 2 strategies.
"""
import json
import strategies.strategy_handling as strats_handl
import strategies.strategies as strats

def get_index(previous_moves_1:list, previous_moves_2:list,
              moves_back:int):
    """Based on the data tuple the according index in the strategy list is
    returned to determine the next move"""
    table_input = previous_moves_1[-moves_back:] + \
                  previous_moves_2[-moves_back:]

    # To indicate the end of the normal options and the start of the inputs
    # when the game just starts
    n = 2 ** (moves_back * 2)
    if all(i == "-" for i in table_input):
        return n
    elif "-" in table_input:
        table_input = [i for i in table_input if i != "-"]
        return n + 1 + strats_handl.base_k_to_integer(table_input, 2)

    # Regular case when the game is in progress for a while
    return strats_handl.base_k_to_integer(list(table_input), 2)

def calculate_payoff(move1, move2, payoff_dict):
    """Calculates the payoff for each strat by comparing their moves and
    looking the payoff for them in the payoff dictionary"""
    if not (move1 in [0, 1] and move2 in [0, 1]):
        print("You seem to be using invalid moves:")
        print("Move1:", move1)
        print("Move2:", move2)

    string = f"{move1}{move2}"
    return payoff_dict[string][0], payoff_dict[string][1]

def battle(strategy_table, strategy_func, rounds, verbose=False):
    """This function executes the battle between a strategy table and strategy
    function and returns the payoff for both strategies after the number of
    rounds. """

    # Open and read the JSON file
    with open('./parameters/parameters.json', 'r') as file:
        data = json.load(file)

    # Extracting the payoff dictionary
    payoff_dict = data["payoff"]
    history_len = data["history_len"]

    # supposed length is 2**(2 * history_len) + 5,
    # 2**(2 * history_len) for the history of both
    # strats and 5 moves for what happends at the start of the game
    supposed_n = 2 ** (2 * history_len) + 5

    if not callable(strategy_table):
        ruletable_arr = strats_handl.integer_2_binary(strategy_table, supposed_n)

    previous_moves_table = []
    previous_moves_func = []

    # append history_len None moves to the history
    for _ in range(history_len):
        previous_moves_table.append("-")
        previous_moves_func.append("-")

    total_payoff_table = 0
    total_payoff_func = 0
    for round in range(rounds):
        # determining the index based on current history for the table
        # strategy. This strategy requires the index in its table to find the
        # according next move.
        if not callable(strategy_table):
            index_table = get_index(previous_moves_table, previous_moves_func,
                                    history_len)

            # Determining the moves and their resulting payoffs
            move_table = ruletable_arr[index_table]
        else:
            move_table = strategy_table(previous_moves_func,
                                        previous_moves_func)
        move_func = strategy_func(previous_moves_table, previous_moves_func)

        payoff_table, payoff_func = calculate_payoff(move_table, move_func,
                                                     payoff_dict)

        # Adjusting the total payoffs
        total_payoff_table += payoff_table
        total_payoff_func += payoff_func

        # Adjusting the history
        previous_moves_table.append(move_table)
        previous_moves_func.append(move_func)
        if verbose:
            print(f"Round {round}")
            print(f"Move table = {move_table} and Move func = {move_func}")
            print(f"Current Payoff table", total_payoff_table,
                  "\n func:", total_payoff_func)
            print("")

    return total_payoff_table, total_payoff_func

def tournament(poule:list, strategies:list):
    """This function runs a tournament by letting each strategy in the poule
    battle against all strategies in strategies. Strategies within the
    poule don't battle each other and strategies within the strategies variable
    also don't.
    This function returns a list of tuples with payoff's from high to low and
    their according strategy in the poule (the strategies list is just to
    have a reference of the effectivity of each strategy)"""

    with open('./parameters/parameters.json', 'r') as file:
        data = json.load(file)

    rounds = data["iterationsPerGame"]

    result = []
    for table_strat in poule:
        total_payoff_table = 0
        for strat_func in strategies:
            payoff_table, _ =  battle(table_strat, strat_func, rounds)
            total_payoff_table += payoff_table
        result.append((total_payoff_table, table_strat))
    result = sorted(result, key=lambda x: x[0], reverse=True)
    return result

def everyone_v_everyone(strategies:list):
    with open('./parameters/parameters.json', 'r') as file:
        data = json.load(file)

    rounds = data["iterationsPerGame"]

    results = {}
    while 1:
        if strategies == []:
            break
        strat_1 = strategies[0]
        strategies.remove(strat_1)

        for strat_2 in strategies:
            payoff_1, payoff_2 =  battle(strat_1, strat_2, rounds)
            if not strat_1 in results:
                results[strat_1] = payoff_1
            else:
                results[strat_1] += payoff_1

            if not strat_2 in results:
                results[strat_2] = payoff_2
            else:
                results[strat_2] += payoff_2
    return results

diy_strats = [767474, strats.always_coop, strats.always_defect,
              strats.defect_last_two_moves_defect,
              strats.defect_last_two_moves_coop,
              strats.alternate, strats.double_alternate,
              strats.inverse, strats.grudge,
              strats.forgiving_grudge, strats.fair_game,
              strats.tit4tat]


resulting_dict = everyone_v_everyone(diy_strats)
list_from_dict = list(resulting_dict.items())
result = sorted(list_from_dict, key=lambda x: x[1], reverse=True)
print(result)
