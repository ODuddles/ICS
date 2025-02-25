import numpy as np
from pyics import Model
import sys
import matplotlib.pyplot as plt
np.random.seed(9021019)
np.set_printoptions(threshold=sys.maxsize)


class CASim(Model):
    def __init__(self):
        Model.__init__(self)

        self.make_param('r', 2)



    def setter_rule(self, val):
        """Setter for the rule parameter, clipping its value between 0 and the
        maximum possible rule number."""
        self.transients = []
        self.cycles = []
        rule_set_size = self.k ** (2 * self.r + 1)
        max_rule_number = self.k ** rule_set_size
        return max(0, min(val, max_rule_number - 1))

    # def build_rule_set(self):
    #     """Sets the rule set for the current rule.
    #     A rule set is a list with the new state for every old configuration.

    #     For example, for rule=34, k=3, r=1 this function should set rule_set to
    #     [0, ..., 0, 1, 0, 2, 1] (length 27). This means that for example
    #     [2, 2, 2] -> 0 and [0, 0, 1] -> 2."""
    #     rule_set_size = self.k ** (2 * self.r + 1)
    #     # small_arr = decimal_to_base_k(self.rule, self.k)
    #     # length_over = rule_set_size - len(small_arr)

    #     # # If you're rule set returned from decimal_to_base_k is too large
    #     # if length_over < 0:
    #     #     print("You're rule number is too large")
    #     #     exit(1)

    #     # Prepending 0's
    #     # self.rule_set = [0 for _ in range(length_over)] + small_arr

    # def build_rule_set_lambda(self):
    #     """Sets the rule set for the current lambda parameter.
    #     A rule set is a list with the new state for every old configuration.

    #     For example, for rule=34, k=3, r=1 this function should set rule_set to
    #     [0, ..., 0, 1, 0, 2, 1] (length 27). This means that for example
    #     [2, 2, 2] -> 0 and [0, 0, 1] -> 2."""
    #     rule_set_size = self.k ** (2 * self.r + 1)
    #     target_lambda = self.lambda_val

    #     if len(self.rule_set) == 0:
    #         self.rule_set = np.zeros(rule_set_size)
    #     previous_rule_set = self.rule_set
    #     previous_lambda = calculate_lambda(0, previous_rule_set)
    #     print("Already calculated lambda:", previous_lambda)

    #     if self.lambda_val > 1:
    #         print("lambda larger than 1.0 is IGNORED")
    #         return

    #     to_change = round((target_lambda - previous_lambda) * rule_set_size)

    #     if to_change >= 0:
    #         s_q_pos = [i for i, x in enumerate(previous_rule_set) if x == 0]
    #         chosen = np.random.choice(s_q_pos, to_change, replace=False)
    #         for choice in chosen:
    #             s_p = np.random.randint(1, self.k)
    #             self.rule_set[choice] = s_p
    #     else:
    #         not_s_q = [i for i, x in enumerate(previous_rule_set) if x != 0]
    #         chosen = np.random.choice(not_s_q, abs(to_change), replace=False)
    #         for choice in chosen:
    #             self.rule_set[choice] = 0



    # def check_rule(self, inp):
    #     """Returns the new state based on the input states.

    #     The input state will be an array of 2r+1 items between 0 and k, the
    #     neighbourhood which the state of the new cell depends on."""
    #     rule_set_size = self.k ** (2 * self.r + 1)
    #     return self.rule_set[rule_set_size - 1 - \
    #                          base_k_to_integer(inp, self.k)]

    # def setup_initial_row(self):
    #     """Returns an array of length `width' with the initial state for each
    #     of the cells in the first row. Values should be between 0 and k."""
    #     if not self.random:
    #         res = np.zeros(self.width)
    #         index = math.floor(self.width / 2)
    #         res[index] = self.k - 1
    #     if self.random:
    #         res = [np.random.randint(0, self.k) for _ in range(self.width)]
    #     return res

    def reset(self):
        """Initializes the configuration of the cells and converts the entered
        rule number to a rule set."""
        self.r = 0


    def draw(self):
        """Draws the current state of the grid."""

        return

    # def step(self):
    #     """Performs a single step of the simulation by advancing time (and thus
    #     row) and applying the rule to determine the state of the cells."""
    #     # Adding new line to the history dictionary
    #     try:
    #         last_t = self.history[np.array2string(self.config[self.t],
    #                                               separator='')[1:-1]]
    #         self.transients.append(last_t)
    #         self.cycles.append(self.t - last_t)

    #         # Stop when the first cycle has been found for the first time
    #         if not self.cycle_hit:
    #             self.cycle_hit = True
    #             return True

    #         success = True
    #     except KeyError:
    #         self.history[np.array2string(self.config[self.t], separator='')
    #                      [1:-1]] = self.t
    #         success = False

    #     self.t += 1

    #     if self.t >= self.height:
    #         self.cycles.append(0)
    #         self.transients.append(0)
    #         self.t -= 1
    #         return True

    #     for patch in range(self.width):
    #         # We want the items r to the left and to the right of this patch,
    #         # while wrapping around (e.g. index -1 is the last item on the
    #         # row). Since slices do not support this, we create an array with
    #         # the indices we want and use that to index our grid.
    #         indices = [i % self.width
    #                    for i in range(patch - self.r, patch + self.r + 1)]
    #         values = self.config[self.t - 1, indices]
    #         self.config[self.t, patch] = self.check_rule(values)

    #     # Stop when a cycle has been found but since this is at the end of
    #     # the function it allows for 1 more graphic demonstration of the next
    #     # step
    #     if success:
    #         return True

if __name__ == '__main__':
    sim = CASim()
    from pyics import GUI
    cx = GUI(sim)
    cx.start()