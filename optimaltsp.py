#!/usr/bin/env python3
"""Run and time an optimal TSP solution."""

import sys
import timeit
import itertools

import tspinput

RUNS = 3

data = tspinput.get(sys.argv[1])

setup = """
import math

def cost(route):
    sum = 0
    # Go back to the start when done.
    route.append(route[0])
    while len(route) > 1:
        p0, *route = route
        sum += math.sqrt((int(p0[0]) - int(route[0][0]))**2 + (int(p0[1]) - int(route[0][1]))**2)
    return sum
"""

code = """
d = float("inf")
for p in itertools.permutations("""+data+"""):
    c = cost(list(p))
    if c <= d:
        d = c
        pmin = p
print("Optimal route:", pmin)
print("Length:", d)
"""

print("Time (seconds, avg of {runs}):".format(runs=RUNS), timeit.timeit(code, setup, number=RUNS)/RUNS)
