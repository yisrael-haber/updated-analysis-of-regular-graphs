from Tryout import graph_creator_regular_next_one
from intersection import intersection
from prepare_full_graph import prepare_full_graph


def restrict_to_regular(n, degree):
    our_graph = graph_creator_regular_next_one(n, degree)
    while intersection(our_graph, degree) > 0:
        our_graph = graph_creator_regular_next_one(n, degree)
    return prepare_full_graph(our_graph)