import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import sys
from tqdm import tqdm

from intersection import intersection
from Main_File import graph_creator_regular_next_one

# A general way to calculate how much intersection seems to happen for certain sizes of graphs.
# Averages out for each size depending on how much accuracy you want. (The values calculated are
# done in direct proportion of the number of nodes in the graphs.)
def intersect_checker(start, jump, jump_num, acc):
    val_vec = []
    for i in tqdm(range(jump_num)):
        inter = [(intersection(graph_creator_regular_next_one(start+i*jump, 4))/acc) for j in range(acc)]
        val_vec += [sum(inter)/(start+i*jump)]
    return val_vec


# Calculates how many nodes are candidates for removal in our random 4-regular graphs, averages out
# for a certain accuracy.
def for_count(n, reps):
    results = []
    for i in range(reps):
        a, b = forward_counter(n)
        results += [b]
    return sum(results)/reps


# This calculates the amount of candidates for removal, creates a function for this amount based on
# the fraction of nodes for removal to the size of the graph.
def for_dist(start, jump, jump_num, acc):
    val_vec = []
    for i in tqdm(range(jump_num)):
        val_vec += [for_count(start + i*jump, acc)]
    return val_vec


# Needs details
def intersection_dist(n, num_of_iter):
    results = [intersection(graph_creator_2(n)) for i in tqdm(range(num_of_iter))]
    a = []
    for i in tqdm(range(n+1)):
        a += [results.count(i)]
    return a


# Normalizes natural number values to a distribution, up to a certain cut-off,
# where we know that afterwards hasevents with probability 0. This is to cut on very long
# unnecessary computations.
def dist_norm(lister, num_of_cutoff):
    summer = sum(lister[:num_of_cutoff])
    return [lister[i]/summer for i in tqdm(range(np.min([num_of_cutoff, len(lister)])))]


def forward_counter(n):
    G = graph_creator_regular_next_one(n, 4)
    for_count = 0
    nodes_to_remove = []
    for i in range(n):
        adjacent = list(G.adj[i])
        if i < adjacent[0]:
            for_count += 1
        if for_count == 2:
            nodes_to_remove.append(i)
            for_count = 0
            continue
        if i < adjacent[1]:
            for_count += 1
        if for_count == 2:
            nodes_to_remove.append(i)
            for_count = 0
    return nodes_to_remove, len(nodes_to_remove)/n


# Creates the Poisson distribution up to a given n.
def poi_dist(lam, n):
    dist_list = []
    factorial = 1
    lam_exp = 1
    for i in range(n):
        dist_list +=[np.exp(-lam)*lam_exp/(factorial)]
        factorial *= (1+i)
        lam_exp *= lam
    return dist_list


# Checks how many times the intersections between the hamiltonian cycles
# happen consecutively. This is to see whether this has any say in the
# combinatorial calculations to prove whether or not the desired distribution
# really is Poi(2) or not.
def intersection_together(n, num_of_iter):
    num = [0, 0]
    for i in tqdm(range(num_of_iter)):
        our_graph = graph_creator_regular_next_one(n, 4)
        deg = list(our_graph.degree())
        deg_list = [val for (node, val) in deg]
        if deg_list.count(2) == 0:
            num[0] += 1
        else:
            num[1] += 1
    return [num[0]/num_of_iter, num[1]/num_of_iter]


def main():
    #   circ_dist = dist_norm(intersection_dist(100000, 2000), 10)
    #   plt.plot(circ_dist)
    #   plt.plot(poi_dist(2, 40))
    #   plt.show()
    shattering_of_four_regular_graphs_5(5000)


if __name__ == '__main__':
    main()