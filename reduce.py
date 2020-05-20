import timeit
import functools


def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]

reduced_values = functools.reduce(calc_values, numbers)

print(reduced_values)

