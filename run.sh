#!/bin/bash
# Run the TSP solutions over randomized input.

# Generate input files.
./generate_input.py

# Run the optimal solution.
echo "## Optimal: 6 points"
echo
./optimaltsp.py tsp6.txt | tail -3
echo
echo "## Optimal: 9 points"
echo
./optimaltsp.py tsp9.txt | tail -3
echo
echo "## Optimal: 10 points"
echo
./optimaltsp.py tsp10.txt | tail -3
echo

# Run the nearest-neighbor solution.
echo "## Nearest neighbor: 9 points"
echo
./nearestneighbor.py tsp9.txt | tail -3
echo
echo "## Nearest neighbor: 1500 points"
echo
./nearestneighbor.py tsp1500.txt | tail -3 | grep -v route
echo
echo "## Nearest neighbor: 3000 points"
echo
./nearestneighbor.py tsp3000.txt | tail -3 | grep -v route
echo
echo "## Nearest neighbor: 9000 points"
echo
./nearestneighbor.py tsp9000.txt | tail -3 | grep -v route

# Clean up
./clean.sh >/dev/null
