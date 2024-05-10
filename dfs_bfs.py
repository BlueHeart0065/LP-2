from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addedges(self , u ,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def dfs_util(self , v , visited ):
        visited[v] = True
        print(v , end =" ")
        
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i , visited)
        
    def dfs(self , v):
        visited = [False]*len(self.graph)
        self.dfs_util(v , visited)
        
    def bfs(self , v):
        visited = [False]*len(self.graph)
        queue = []
        queue.append(v)
        visited[v] = True
    
        while queue:
            v = queue.pop(0)
            print(v , end = " ")
            
            for i in self.graph:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        
n = int(input("enter the no. of nodes:"))
g = Graph()
for i in range(n):
    a = int(input("ente the 1st node :"))
    b = int(input("ente the 2nd node :"))
    g.addedges(a,b)
    
p = int(input("enter the starting point:"))
g.dfs(p)
    
q = int(input("enter the starting point:"))

g.bfs(q)