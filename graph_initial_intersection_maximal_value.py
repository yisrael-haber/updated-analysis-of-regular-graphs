import numpy as np
from matplotlib import pyplot as plt

from initial_intersection_maximal_value import initial_intersection_maximal_value


def graph_out_initial_intersection_maximal_value(first_num, last_num, jump_num):
    len_of_nums_to_check = int(np.floor((last_num-first_num)/jump_num)) + 1
    list_of_values_to_check = [first_num + i*jump_num for i in range(len_of_nums_to_check)]
    list_of_vals = [initial_intersection_maximal_value(value) for value in list_of_values_to_check]
    plt.plot(list_of_values_to_check, list_of_vals)
    plt.show()
    return list_of_vals