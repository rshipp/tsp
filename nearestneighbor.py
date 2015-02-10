#!/usr/bin/env python3
"""Run and time a nearest neighbor TSP solution."""

import sys
import timeit

import tspinput

RUNS = 3

data = tspinput.get(sys.argv[1])

setup = """
import math

def closestpoint(point, route):
    dmin = float("inf")
    for p in route:
        d = math.sqrt((int(point[0]) - int(p[0]))**2 + (int(point[1]) - int(p[1]))**2)
        if d < dmin:
            dmin = d
            closest = p
    return closest, dmin
"""

code = """
point, *route = """+data+"""
path = [point]
sum = 0
while len(route) >= 1:
    closest, dist = closestpoint(path[-1], route)
    path.append(closest)
    route.remove(closest)
    sum += dist
# Go back the the beginning when done.
closest, dist = closestpoint(path[-1], [point])
path.append(closest)
sum += dist

print("Optimal route:", path)
print("Length:", sum)
"""

print("Time (seconds, avg of {runs}):".format(runs=RUNS), timeit.timeit(code, setup, number=RUNS)/RUNS)
