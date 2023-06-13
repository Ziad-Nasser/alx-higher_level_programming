#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la, lb = len(tuple_a), len(tuple_b)
    if (la == 0):
        tuple_a = (0, 0)
    elif la < 2:
        tuple_a += 0,
    if (lb == 0):
        tuple_b = (0, 0)
    elif lb < 2:
        tuple_b += 0,
    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
