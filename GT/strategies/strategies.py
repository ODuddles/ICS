""""
Owen Duddles 15099261
Narek Wartanian 14787148

This file contains all of the strategies that will be used in tournament.
Each strategy receives two lists:
    previous_opp: A list containing the previous moves of the opponent.
    previous_self: A list containing the previous moves of myself.
"""


def always_coop(previous_opp: list, previous_self: list):
    """
        Always cooperates with the opponent.
    """
    return 0


def always_defect(previous_opp: list, previous_self: list):
    """
        Always deflect the opponent.
    """
    return 1


def defect_last_two_moves_defect(previous_opp: list, previous_self: list):
    """
        Looks at the last two moves of the opponent, if the moves are
        deflections return a defection, else a cooperation is returned.
    """
    real = previous_opp[::-1]
    if real[:2] == [1, 1]:
        return 1
    else:
        return 0


def sneaky_tit4tat(previous_opp: list, previous_self: list):
    """
        Looks at the last two moves of the opponent, if the moves are
        cooperation return a defection, else a cooperation is returned.
    """
    real = previous_opp[::-1]
    if real[:2] == [0, 0]:
        return 1

    if real[0] == 1:
        return 1
    else:
        return 0


def alternate(previous_opp: list, previous_self: list):
    """
        Alternates between cooperate and defect.
    """
    real = previous_self[::-1]
    if real[0]:
        return 0
    else:
        return 1


def double_alternate(previous_opp: list, previous_self: list):
    """
        Alternates by looking at its own last two moves 0,0 -> 1,1 etc.
    """
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


def eye_4_eye(previous_opp: list, previous_self: list):
    """
        When the opponent defects, this strategy defects as many times as the
        opponent has defect up until this point in the game
    """
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


def grudge(previous_opp: list, previous_self: list):
    """
        Once the oponnent returns a defect once, grudge will always
        return a grudge from that point on.
    """
    if 1 in previous_opp:
        return 1
    else:
        return 0


def forgiving_grudge(previous_opp: list, previous_self: list):
    """
        The same as grudge, but this time the function will forgive the
        opponnent if het makes up to the function by not defecting 5 times
        in a row.
    """
    real = previous_opp[::-1]
    if 1 in real[:6]:
        return 1
    else:
        return 0


def fair_game(previous_opp: list, previous_self: list):
    """
        This strategy will cooperate as long as the oponnent cooperates
        for atleast 50%+ else it will defect.
    """
    defect_amount = previous_opp.count(1)
    cooperate_amount = previous_opp.count(0)

    if cooperate_amount > defect_amount:
        return 0
    else:
        return 1


def tit4tat(previous_opp: list, previous_self: list):
    """
        This strategy will cooperate as long as the oponnent cooperates
        for atleast 50%+ else it will defect.
    """
    real = previous_opp[::-1]
    if real[0] == 1:
        return 1
    else:
        return 0
