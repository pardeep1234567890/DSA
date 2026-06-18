# class Solution:
#     def findRedundantConnection(self, edges):
#         parent = [i for i in range(len(edges)+1)] 

#         def find(x):
#             while parent[x] != x:
#                 x = parent[x]    
#             return x

#         def Union(x,y):
#             px = find(x)
#             py = find(y)
#             if px == py :
#                 return False 
#             parent[px] = py
#             return True

#         for u,v in edges:
#             if find(u) == find(v):
#                 return [u,v]
#             Union(u,v)

class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges)+1)] 

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]

        def Union(x,y):
            px = find(x)
            py = find(y)
            if px == py :
                return False 
            parent[px] = py
            return True

        for u,v in edges:
            if find(u) == find(v):
                return [u,v]
            Union(u,v)