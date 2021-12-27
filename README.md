This was my very first Python project and I started learning Python by working on this project. This is why I didn't use numpy or practical built-ins. At this point, I only new the syntax. However, the implemented algorithms work.

# How To:

All algorithms can be used in the script main.py.


## `greedy(varCosts,fixCosts,potentialLocs)` 

Finds a heuristic solution for the warehouse location problem. It prints a table with information in each iteration.

### Parameters

- varCosts: 2d-list where varCosts[i,j] is the cost for transporting one unit from i to j.
- fixCosts: List where fixCosts[i] marks the fix costs for opening a warehouse at location i.
- potentialLocs: List of 1-based indices of potential warehouse locations. 

### Return

- X: List of 1-based indices of warehouse locations which are part of the heuristic solution. 

## `weiszfeld(vectors, weights,d)`

Uses Weiszfeld's algorithm to approximate the solution of a 1-median-problem with euclidian metric.

### Parameters

- vectors: 2-d list with all locations on a plane.

### Return

- X: List of 1-based indices of warehouse locations which are part of the heuristic solution. 
