def sorted_four_contains_overlap(sorted_list):
    if sorted_list[0] == sorted_list[1]:
        return True
    if sorted_list[1] == sorted_list[2]:
        return True
    if sorted_list[2] == sorted_list[3]:
        return True
    return False