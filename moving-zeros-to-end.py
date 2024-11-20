def move_zeros(lst):
    c = lst.count(0)
    l = list(filter(lambda x: x != 0, lst))
    l.extend([0]*c)
    return l