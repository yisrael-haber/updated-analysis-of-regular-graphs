from prepare_full_graph import prepare_full_graph


def intersection(unicycle_graph, degree):
    d_graph = prepare_full_graph(unicycle_graph)
    edge_num = len(d_graph.edges)
    return 0.5 * degree * (len(list(d_graph.nodes))) - edge_num