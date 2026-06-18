class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node):
        if not node :   # Edge case : empty Graph
            return
        clone_hashmap = {}
        def dfs(n):
            if n in clone_hashmap:  # Base case : already cloned 
                return clone_hashmap[n]
            clone_hashmap[n] = Node(n.val) # clone the node 

            for neighbor in n.neighbors:  # connect cloned neighbors 
                clone_hashmap[n].neighbors.append(dfs(neighbor))
            return (clone_hashmap[n])     # Return the clone 
        return dfs(node)         