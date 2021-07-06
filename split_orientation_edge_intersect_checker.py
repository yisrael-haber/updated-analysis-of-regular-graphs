import numpy as np
from tqdm import tqdm

from simple_edge_intersect_checker_split_orientation import simple_edge_intersect_checker_split_orientation


def split_orientations_edge_intersect_checker(our_graph):
    edges_of_graph = list(our_graph.edges)
    num_of_edges = len(edges_of_graph)
    edge_orientation = [np.random.binomial(1, 0.5) for i in range(num_of_edges)]
    edges_that_intersect_per_node = [set() for _ in range(len(our_graph.nodes))]
    for i in tqdm(range(num_of_edges)):
        first_edge = edges_of_graph[i]
        for j in range(num_of_edges - i - 1):
            second_edge = edges_of_graph[i + j + 1]
            if simple_edge_intersect_checker_split_orientation(first_edge, second_edge, edge_orientation[i], edge_orientation[i+ j + 1]):
                edges_that_intersect_per_node[first_edge[0]].add((first_edge, second_edge))
                edges_that_intersect_per_node[first_edge[1]].add((first_edge, second_edge))
                edges_that_intersect_per_node[second_edge[0]].add((first_edge, second_edge))
                edges_that_intersect_per_node[second_edge[1]].add((first_edge, second_edge))
    return edges_that_intersect_per_node