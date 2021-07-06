import networkx as nx
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

# Bringing Refactored functions to use, refactored for visual reasons
from for_hamiltonian_cycle import for_hamiltonian_cycle
from random_matching import random_matching


def two_sorter(a, b):
    if a < b:
        return a, b
    return b, a


# Creating a random cycle graph or random matching using the np.random.permutation function, much faster
# than the previous version.
def graph_creator_regular_next_one(n, degree):
    G = nx.Graph()
    edges_to_add = set()
    edges_to_add |= set([(i % n, (i+1) % n) for i in range(n)] + [((i + 1) % n, i % n) for i in range(n)])
    while len(edges_to_add) != (2*(degree//2)*n):
        new_edges = for_hamiltonian_cycle(edges_to_add, n)
        if len(new_edges) == len(edges_to_add):
            continue
        edges_to_add = new_edges.copy()
    if degree % 2 == 1:
        while len(edges_to_add) != n * degree:
            new_edges = random_matching(edges_to_add, n)
            if new_edges == 0:
                continue
            edges_to_add = new_edges.copy()
    G.add_edges_from(edges_to_add)
    return G


# the function that calculates whether 2 edges between nodes in a cycle will intersect or not
def simple_edge_intersect_checker(edge_1, edge_2):
    fefn, fesn = two_sorter(edge_1[0], edge_1[1])
    sefn, sesn = two_sorter(edge_2[0], edge_2[1])
    return (fefn < sefn < fesn < sesn) or (sefn < fefn < sesn < fesn)


# for a graph with the trivial cycle it calculates for every node in which
# tuples of edges that intersect it appears. this is important for the next
# function.
def complicated_edge_intersect_checker_no_change(our_graph):
    edges_of_graph = list(our_graph.edges)
    num_of_edges = len(edges_of_graph)
    edges_that_intersect_per_node = [set() for _ in range(len(our_graph.nodes))]
    for i in tqdm(range(num_of_edges)):
        first_edge = edges_of_graph[i]
        for j in range(num_of_edges-i-1):
            second_edge = edges_of_graph[i+j+1]
            if simple_edge_intersect_checker(first_edge, second_edge):
                edges_that_intersect_per_node[first_edge[0]].add((first_edge, second_edge))
                edges_that_intersect_per_node[first_edge[1]].add((first_edge, second_edge))
                edges_that_intersect_per_node[second_edge[0]].add((first_edge, second_edge))
                edges_that_intersect_per_node[second_edge[1]].add((first_edge, second_edge))
    return edges_that_intersect_per_node


def check_shattering(our_graph, threshold):
    size_of_gcc = len(sorted(nx.connected_components(our_graph), key=len, reverse=True)[0])
    if size_of_gcc <= threshold:
        return True
    return False


def initialize_basic_params_for_planarization(n, degree):
    created_graph = graph_creator_regular_next_one(n, degree)
    edges_intersect_per_node = complicated_edge_intersect_checker_no_change(created_graph)
    sum_per_node = [len(edges_intersect_per_node[i]) for i in range(len(edges_intersect_per_node))]
    checker = False
    counter = 0
    perc_values = []
    y_values = []
    gcc_size_values = []
    return created_graph, edges_intersect_per_node, sum_per_node, checker, counter, perc_values, y_values, gcc_size_values



# Creates a random graph with 2 non-intersecting random hamilton cycles. Then for each node
# it takes the input from the previous function in order to remove nodes with the highest
# amount of intersection it is involved in. The list from the previous function is in order
# to keep track of what nodes interact with other nodes, and how often.
def planarization_of_assymptotic_regular_graphs_optimized(n, degree, perc_checker):
    our_graph, edges_intersect_per_node, sum_per_node, checker, counter, perc_values, max_per_node_values, gcc_size_values = initialize_basic_params_for_planarization(n, degree)
    while not np.amax(sum_per_node) == 0:
        best_node = np.argmax(sum_per_node)
        interactions = edges_intersect_per_node[best_node]
        for key in interactions:
            nodes_inter = [key[0][0], key[0][1], key[1][0], key[1][1]]
            index_of_best_node = nodes_inter.index(best_node)
            for index in range(4):
                if index != index_of_best_node:
                    node_of_interest = nodes_inter[index]
                    edges_intersect_per_node[node_of_interest].remove(key)
        edges_intersect_per_node[best_node] = set()
        our_graph.remove_node(best_node)
        counter += 1
        sum_per_node = [len(edges_intersect_per_node[i]) for i in range(len(edges_intersect_per_node))]
        if counter % (perc_checker*n) == 0:
            checker = (nx.check_planarity(our_graph)[0])
            perc_values += [100 * counter/n]
            max_per_node_values += [np.amax(sum_per_node)]
            gcc_size_values += [len(sorted(nx.connected_components(our_graph), key=len, reverse=True)[0])]
            print(f"\nYou have removed {100 * counter/n} percent of the nodes, the maximal value of intersections is {np.amax(sum_per_node)}")
            print(f"The graph is shattered? {check_shattering(our_graph, np.sqrt(n))}")
    print(f"The planarized graph has {len(list(our_graph.nodes))/n} nodes left")
    return our_graph, perc_values, max_per_node_values, gcc_size_values


# Planarazation of a 4 regular graph by continuously removing the node with highest degree
# which is what the article suggested to do.
def max_degree_planarization(n, degree):
    our_graph = graph_creator_regular_next_one(n, degree)
    counter = 0
    while not (nx.check_planarity(our_graph)[0]):
        if counter % (0.01*n) == 0:
            print(counter / (0.01*n))
        our_degrees = our_graph.degree()
        nodes = [node for (node, val) in our_degrees]
        degrees = [val for (node, val) in our_degrees]
        index_of_top_node = np.argmax(degrees)
        our_graph.remove_node(nodes[index_of_top_node])
        counter += 1
    print(len(list(our_graph.nodes))/n)
    return our_graph


def main():
    #   print(initial_intersection_maximal_value(1000))
    #   print(shattering_of_four_regular_graphs_no_change(2000))
    our_graph, x_vals, y_vals, gcc_size_values = planarization_of_assymptotic_regular_graphs_optimized(3000, 10, 0.005)
    plt.plot(x_vals, y_vals)
    plt.show()
    plt.plot(x_vals, gcc_size_values)
    plt.show()


if __name__ == '__main__':
    main()