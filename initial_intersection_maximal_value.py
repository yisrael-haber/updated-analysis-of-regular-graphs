import numpy as np

from Tryout import complicated_edge_intersect_checker_no_change
from restrict_to_regular import restrict_to_regular


def initial_intersection_maximal_value(len_of_cycle):
    our_graph = restrict_to_regular(len_of_cycle)
    edges_intersect_per_node = complicated_edge_intersect_checker_no_change(our_graph)
    sum_per_node = [len(edges_intersect_per_node[i]) for i in range(len(edges_intersect_per_node))]
    return np.amax(sum_per_node)