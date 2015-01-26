#!/usr/bin/env python3
"""Generate randomized input files, in the expected format."""

import itertools
from random import randint

MIN = 0
MAX = 500

def generate_input(n, filename):
    with open(filename, "w") as f:
        f.write("{n}\n".format(n=n))
        for _ in itertools.repeat(None, n):
            f.write("{p0} {p1}\n".format(p0=randint(MIN, MAX), p1=randint(MIN, MAX)))

if __name__ == "__main__":
    # Write the input files for the optimal solution first.
    n = 6
    generate_input(n, "tsp6.txt")
    n = 9
    generate_input(n, "tsp9.txt")
    n = 10
    generate_input(n, "tsp10.txt")
    # Then write the input files for nearest neighbor.
    n = 1500
    generate_input(n, "tsp1500.txt")
    n = 3000
    generate_input(n, "tsp3000.txt")
    n = 9000
    generate_input(n, "tsp9000.txt")
