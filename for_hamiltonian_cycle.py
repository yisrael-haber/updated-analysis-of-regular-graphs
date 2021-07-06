import numpy as np

import intersection


def for_hamiltonian_cycle(edges_we_will_add, n):
    new_perm = np.random.permutation(n)
    new_edges = set([(new_perm[i % n], new_perm[(i + 1) % n]) for i in range(n)] + [(new_perm[(i + 1) % n], new_perm[i % n]) for i in range(n)])
    if len(edges_we_will_add.intersection(new_edges)) == 0:
        edges_we_will_add |= new_edges
    return edges_we_will_add