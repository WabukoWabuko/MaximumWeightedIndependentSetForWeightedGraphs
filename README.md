# MaximumWeightedIndependentSetForWeightedGraphs
## Question
Consider a graph G=(V, E) where V is a set of vertices and E is a set of edges. The graph is weighted and undirected. Develop an algorithm to find the maximum weighted independent set in G. The independent set is a set of vertices where no two vertices are connected by an edge. The weight of an independent set is the sum of the weights of its vertices. The goal is to find an independent set with the maximum total weight. The algorithm should run in polynomial time and have a space complexity of O(n).

Note: This is a well-known problem in graph theory and computer science and has applications in many areas, including scheduling, resource allocation, and network design.

## Solution
Let's assume that the vertices in G are numbered from 1 to n. Let w(i) be the weight of vertex i, and let S be a set of vertices. We will use A(S) to represent the maximum weight of an independent set in the subgraph induced by the vertices in S.

The algorithm is as follows:

Initialize A({}) = 0 and A({i}) = w(i) for all vertices i in G.

For all sets S with at least two vertices, compute A(S) as follows:

a. If vertex n is not in S, then A(S) = A(S-{n}).

b. If vertex n is in S, then A(S) = max{A(S-{n}), A(S-{n}-N(n))+w(n)}, where N(n) is the set of neighbors of vertex n.

Return the set of vertices that correspond to the maximum weight, which can be computed from the A matrix.

The time complexity of this algorithm is O(2^n), which is not efficient for large graphs. However, we can optimize the algorithm by using memoization to store previously computed values. This reduces the time complexity to O(n^2). The space complexity is O(n) since we only need to store A(S) for each set S.
