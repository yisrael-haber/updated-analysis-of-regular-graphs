def sortFour(a, b, c, d):
    if a < b:
        low1 = a
        high1 = b
    else:
        low1 = b
        high1 = a
    if c < d:
        low2 = c
        high2 = d
    else:
        low2 = d
        high2 = c
    if low1 < low2:
        lowest = low1
        middle1 = low2
    else:
        lowest = low2
        middle1 = low1
    if high1 > high2:
        highest = high1
        middle2 = high2
    else:
        highest = high2
        middle2 = high1
    if middle1 < middle2:
        return lowest, middle1, middle2, highest
    else:
        return lowest, middle2, middle1, highest