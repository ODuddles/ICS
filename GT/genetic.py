""""
Owen Duddles 15099261
Narek Wartanian 14787148
This file contains the GenAlgorithm class that is able to:
create random strategies and procreate a new strategies from two
strategies.

"""
import battle
import json
import strategies.strategy_handling as strats_handl
import strategies.strategies as strats
import numpy as np


class GenAlgorithm():
    def __init__(self):
        """Initializes the required elements to the genetic algorithm"""
        self.poule = self.create_random_strats()
        self.diy_strats = [strats.always_coop, strats.always_defect,
                           strats.defect_last_two_moves_defect,
                           strats.sneaky_tit4tat,
                           strats.alternate, strats.double_alternate,
                           strats.eye_4_eye,
                           strats.grudge,
                           strats.forgiving_grudge, strats.fair_game,
                           strats.tit4tat]
        self.gen = 1

    def procreate(self, ruletable1: int, ruletable2: int):
        """Procreates two ruletables and returns their child as an integer.
        The ruletables are procreated by using the first half of one
        of the ruletables and the second half of the other. Who dominates
        the first half and who dominates the second is randomly determined. """
        ruletable1_arr = strats_handl.integer_2_binary(ruletable1, 21)
        ruletable2_arr = strats_handl.integer_2_binary(ruletable2, 21)

        half = int(np.floor(len(ruletable1_arr) / 2))

        bool = np.random.randint(0, 2)
        if bool:
            child = ruletable1_arr[:half] + ruletable2_arr[half:]
        else:
            child = ruletable2_arr[:half] + ruletable1_arr[half:]

        if len(child) != len(ruletable1_arr):
            print("Something went wrong with splitting halves")
            exit()

        return strats_handl.base_k_to_integer(child, 2)

    def create_random_strats(self):
        """Returns a list of random strategies for the start of the
        algorithm"""
        strats = []

        with open('./parameters/parameters.json', 'r') as file:
            data = json.load(file)

        n = data["pool_size"]
        steps_back = data["history_len"]

        for _ in range(n):
            # Note that the 5 only works for steps_back is 1 or 2. If you
            # want the code to be more dynamic, you'll have to change this
            strat = np.random.randint(0, 2**(2 ** (2 * steps_back) + 5) + 1)
            strats.append(strat)
        return strats

    def run_one_gen(self):
        """Runs the poule agains the diy strats in strategies.py. The
        best performing strategies in the poule procreate and as such poule
        is adjusted to contain the next generation"""
        results = battle.tournament(self.poule, self.diy_strats)
        with open("result.txt", "a+") as f:
            f.write(f"{self.gen},{results[0][0]}\n")
        self.gen += 1
        with open("top20.txt", "w") as f:
            for _, result in zip(self.poule, results):
                f.write(f"{result[0]},{result[1]}\n")

        quarter = int(np.floor(len(results) / 4))
        to_procreate = [s for _, s in results[:quarter]]

        new_strats = []
        for table in to_procreate:
            to_procreate_not_self = to_procreate.copy()
            to_procreate_not_self.remove(table)
            for _ in range(3):
                other_parent = np.random.choice(to_procreate_not_self,
                                                size=1)[0]
                child = self.procreate(table, other_parent)
                child = strats_handl.mutate(child)
                new_strats.append(child)

        new_poule = new_strats + to_procreate
        if len(new_poule) < len(results):
            for _ in range(len(results) - len(new_poule)):
                table = np.random.choice(to_procreate_not_self, size=1)[0]
                to_procreate_not_self = to_procreate.copy()
                to_procreate_not_self.remove(table)
                other_parent = np.random.choice(to_procreate_not_self,
                                                size=1)[0]
                child = self.procreate(table, other_parent)
                child = strats_handl.mutate(child)
                new_strats.append(child)

        if len(new_poule) > len(results):
            print("A new generation is larger than the previous")
            exit()
        self.poule = new_poule
