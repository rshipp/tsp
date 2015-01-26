"""Convert TSP input file to required format."""

def get(filename):
    with open(filename, "r") as f:
        f.readline()
        return str([p.split() for p in f.read().strip().splitlines()])
