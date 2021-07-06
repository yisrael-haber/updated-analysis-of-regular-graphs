import networkx as nx
import numpy as np
from tqdm import tqdm

from Tryout import graph_creator_regular_next_one
from split_orientation_edge_intersect_checker import split_orientations_edge_intersect_checker


def shattering_of_four_regular_graphs_split_orientation(n, degree):
    our_graph = graph_creator_regular_next_one(n, degree)
    edges_intersect_per_node = split_orientations_edge_intersect_checker(our_graph)
    while not (nx.check_planarity(our_graph)[0]):
        sum_per_node = [len(edges_intersect_per_node[i]) for i in range(len(edges_intersect_per_node))]
        best_node = np.argmax(sum_per_node)
        interactions = edges_intersect_per_node[best_node]
        for key in tqdm(interactions):
            nodes_inter = [key[0][0], key[0][1], key[1][0], key[1][1]]
            index_of_best_node = nodes_inter.index(best_node)
            for index in range(4):
                if index != index_of_best_node:
                    node_of_interest = nodes_inter[index]
                    edges_intersect_per_node[node_of_interest].remove(key)
        edges_intersect_per_node[best_node] = set()
        our_graph.remove_node(best_node)
    print(len(list(our_graph.nodes))/n)
    return our_graph