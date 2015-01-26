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

### Optimal: 6 points

```
Optimal route: (['441', '203'], ['445', '322'], ['410', '404'], ['186', '267'], ['55', '272'], ['3', '84'])
Length: 796.9525222294839
Time (s): 0.017538285988848656
```

### Optimal: 9 points

```
Optimal route: (['455', '429'], ['449', '441'], ['196', '410'], ['172', '366'], ['318', '240'], ['280', '208'], ['319', '107'], ['441', '150'], ['496', '54'])
Length: 909.2229786949287
Time (s): 9.90254145200015
```

### Optimal: 10 points

```
Optimal route: (['129', '496'], ['418', '470'], ['456', '412'], ['315', '277'], ['335', '250'], ['417', '146'], ['372', '24'], ['314', '56'], ['192', '43'], ['192', '160'])
Length: 1156.721037944675
Time (s): 184.13369058902026
```

### Nearest neighbor: 9 points

```
Optimal route: [['319', '107'], ['280', '208'], ['318', '240'], ['441', '150'], ['496', '54'], ['455', '429'], ['449', '441'], ['196', '410']]
Length: 1066.540054147503
Time (s): 0.00017043598927557468
```

### Nearest neighbor: 1500 points

```
Length: 16866.146326520746
Time (s): 5.113344659999711
```

### Nearest neighbor: 3000 points

```
Length: 24704.32351161239
Time (s): 18.913936911005294
```

### Nearest neighbor: 6000 points

```
Length: 42457.22800258024
Time (s): 149.34464275697246
```
