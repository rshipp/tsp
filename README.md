# Traveling Salesman Problem

Two implementations of solutions to the Traveling Salesman Problem in Python 3.

The first solution brute forces all permutations and is guaranteed to find
the optimal solution for visiting all points.

The second solution is "nearest neighbor", which is much faster, but is not
guaranteed to find the optimal solution. In some edge cases, it finds very poor
solutions.

My implementations of these algorithms display about O(n!) and 1/4 O(n^2) time,
respectively.

## Usage

If you want to run the comparisons yourself, just go

    ./run.sh

Or, if you want to run individual tests, just use `./optimaltsp.py FILENAME` or
`./nearestneighbor.py FILENAME`.

## Graphs

Here are some quick runtime graphs, courtesy of [WolframAlpha](http://www.wolframalpha.com).

### Optimal

[![optimal graph](optimal.png "x-axis is input points; y-axis is seconds")](http://www.wolframalpha.com/input/?i=plot+%286%2C+0.02%29%2C+%288%2C+1.0%29%2C+%289%2C+9.9%29%2C+%2810%2C+184.1%29)

### Nearest neighbor

[![nearest neighbor graph](nn.png "x-axis is input points; y-axis is seconds")](http://www.wolframalpha.com/input/?i=plot%20%289%2C%200%29%2C%20%281500%2C%205%29%2C%20%283000%2C%2019%29%2C%20%286000%2C%20149%29)

## Data

