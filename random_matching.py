import numpy as np


def random_matching(edges_we_will_add, n):
    new_perm = np.random.permutation(n)
    new_edges = set([(new_perm[2 * i], new_perm[2 * i + 1]) for i in range(int(0.5 * n))]+[(new_perm[2 * i + 1], new_perm[2 * i]) for i in range(int(0.5 * n))])
    if len(edges_we_will_add.intersection(new_edges)) == 0:
        edges_we_will_add |= new_edges
    return edges_we_will_add