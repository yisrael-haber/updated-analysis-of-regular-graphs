def prepare_full_graph(unicycle_graph):
    node_nums = len(list(unicycle_graph.nodes))
    graph_edges_to_add = [(i % (node_nums), (i+1) % (node_nums)) for i in range(node_nums)]
    unicycle_graph.add_edges_from(graph_edges_to_add)
    return unicycle_graph