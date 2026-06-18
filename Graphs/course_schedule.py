# Steps of this solution 
# 1. Make the Adjacency List 
# 2. Using Dfs check that there is cycle or not in the Graph 
# 3. we will check for every node using loop because there can be disconnected graph also  
class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for _ in range(numCourses)]  
        state = [0] * numCourses
        for prereq in prerequisites:
            x = prereq[0]
            y = prereq[1]
            adjList[y].append(x) 
        def dfs(node):
            if state[node] ==1:
                return True  
            if state[node] == 2:
                return False
            state[node] = 1
            for nei in adjList[node]:
                if dfs(nei):
                    return True
            state[node] = 2
            return False
        for i in range(numCourses):
            if dfs(i):
                return False
        return True            


# BFS Steps (mental template)
# build graph
# compute indegree
# queue = nodes with indegree 0
# pop from queue
# reduce neighbors indegree
# if indegree becomes 0 → push
# count processed nodes
# if processed == n → True else False

import enum
from collections import deque
class Solution :
    def canFinish(self, numCourses, prerequisities):
        graph =[[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for course,prereq in prerequisities:
            graph[prereq].append(course) 
            indegree[course] += 1
        # queue = deque(i for i , deg in enumerate(indegree) if deg == 0)
        queue = deque()
        visited = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            visited +=1 
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 :
                    queue.append(neighbor)
        return visited == numCourses            