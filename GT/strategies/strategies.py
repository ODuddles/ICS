""""
Owen Duddles 15099261
Narek Wartanian 14787148

This file contains all of the strategies that will be used in tournament.
Each strategy receives two lists:
    previous_opp: A list containing the previous moves of the opponent.
    previous_self: A list containing the previous moves of myself.
"""

import numpy as np

"""
    Always cooperates with the opponent.
"""
def always_coop(previous_opp: list, previous_self: list): return 0


"""
    Always deflect the opponent.
"""
def always_defect(previous_opp: list, previous_self: list): return 1


"""
    Looks at the last two moves of the opponent, if the moves are deflections
    return a defection, else a cooperation is returned.
"""
def defect_last_two_moves_defect(previous_opp: list, previous_self: list):
    real = previous_opp[::-1]
    if real[:2] == [1, 1]:
        return 1
    else:
        return 0


"""
    Looks at the last two moves of the opponent, if the moves are cooperation
    return a defection, else a cooperation is returned.
"""
def sneaky_tit(previous_opp: list, previous_self: list):
    real = previous_opp[::-1]
    if real[:2] == [0, 0]:
        return 1

    if real[0] == 1:
        return 1
    else:
        return 0


"""
    Alternates between cooperate and defect.
"""
def alternate(previous_opp: list, previous_self: list):
    real = previous_self[::-1]
    if real[0]:
        return 0
    else:
        return 1


"""
    Alternates by looking at its own last two moves 0,0 -> 1,1 etc.
"""
def double_alternate(previous_opp: list, previous_self: list):
    real = previous_self[::-1]
    if real[0]:
        if real[:2] == [1, 1]:
            return 0
        else:
            return 1
    elif real[:2] == [0, 0]:
        return 1
    else:
        return 0


"""
    When the opponent defects, this strategy defects as many times as the
    opponent has defect up until this point in the game
"""
def eye_4_eye(previous_opp: list, previous_self: list):
    if previous_self[-1] == 1:
        index = len(previous_self) - 1
        nr_1_self = 0
        while 1:
            if previous_self[index] == 1:
                nr_1_self += 1
            else:
                index += 1
                break
            index -= 1

        if nr_1_self < previous_opp.count(1):
            return 1
    elif previous_opp[-1] == 1:
        return 1
    return 0

"""
    Once the oponnent returns a defect once, grudge will always
    return a grudge from that point on.
"""
def grudge(previous_opp: list, previous_self: list):
    if 1 in previous_opp:
        return 1
    else:
        return 0


"""
    The same as grudge, but this time the function will forgive the
    opponnent if het makes up to the function by not defecting 5 times
    in a row.
"""
def forgiving_grudge(previous_opp: list, previous_self: list):
    real = previous_opp[::-1]
    if 1 in real[:6]:
        return 1
    else:
        return 0


"""
    This strategy will cooperate as long as the oponnent cooperates
    for atleast 50%+ else it will defect.
"""
def fair_game(previous_opp: list, previous_self: list):
    defect_amount = previous_opp.count(1)
    cooperate_amount = previous_opp.count(0)

    if cooperate_amount > defect_amount:
        return 0
    else:
        return 1


"""
    This strategy will cooperate as long as the oponnent cooperates
    for atleast 50%+ else it will defect.
"""
def tit4tat(previous_opp: list, previous_self: list):
    real = previous_opp[::-1]
    if real[0] == 1:
        return 1
    else:
        return 0