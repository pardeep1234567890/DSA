from collections import  deque
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1]* n

        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0
                while queue :
                    node = queue.popleft()
                    for nei in graph[node]:
                        if color[nei] == -1:
                            color[nei] = 1-color[node]
                            queue.append(nei)
                        else:
                            if color[nei] == color[node]:
                                return False           
        return True

# Simple Algorithm to Remember
# Think of it as "2-color painting":

# Pick an unpainted node → paint it Red
# BFS: paint all its neighbors Blue
# Paint their neighbors Red, and so on…
# If you ever find a neighbor that's already the same color as the current node → Not Bipartite
# Repeat for all disconnected components
# One-liner to remember: "Try to 2-color the graph using BFS. If you hit a conflict, it's not bipartite."

# Interview-Ready Explanation
# "A graph is bipartite if we can split its nodes into two groups such that every edge connects a node from one group to the other — no edge within the same group.

# My approach is BFS-based 2-coloring. I maintain a color array initialized to -1 (unvisited). I iterate through all nodes to handle disconnected components. For each unvisited node, I assign it color 0 and start BFS. For every neighbor:

# If unvisited, I assign it the opposite color (1 - current).
# If already colored the same as the current node, we have a conflict — the graph is not bipartite, so I return False.
# If BFS completes for all components without conflict, I return True.

# Time complexity: O(V + E) — we visit every node and edge once.
# Space complexity: O(V) — for the color array and BFS queue."