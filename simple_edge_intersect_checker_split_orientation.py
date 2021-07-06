from Tryout import two_sorter


def simple_edge_intersect_checker_split_orientation(edge_1, edge_2, edge_1_orientation, edge_2_orientation):
    if edge_1_orientation != edge_2_orientation:
        return False
    # the names are initials - for exapmle fefn stands for first edge first node.
    fefn, fesn = two_sorter(edge_1[0], edge_1[1])
    sefn, sesn = two_sorter(edge_2[0], edge_2[1])
    return (fefn < sefn < fesn < sesn) or (sefn < fefn < sesn < fesn)