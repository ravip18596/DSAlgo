# DFS (Depth First Search)

## Find number of connected components in undirected graph

```python
from collections import defaultdict

class Solution:
     def find_connected_components(self, n, edges):
       def dfs(node, graph, visited):
         visited[node] = True
         for neigh in graph[node]:
           if not visited[neigh]:
             dfs(neigh, graph, visited)
        
       graph = defaultdict(list)

       for u,v in edges:
         graph[u].append(v)
         graph[v].append(u)

       visited = [False]*n
       connected_component = 0
       for i in range(n):
         if not visited[i]:
           dfs(i, graph, visited)
           connected_component += 1
           
       return connected_component
```

## Find all paths in directed Acyclic Graph (DAG) when given source and destination

```python
from collections import defaultdict

def dfs(src, dest, graph, path, paths):
    path.append(src)
    if src==dest:
        paths.append(path.copy())
    else:
        for neigh in graph[src]:
            dfs(neigh, dest, graph, path, paths)
    path.pop()
    
def find_paths(v, edges, src, dest):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        
    paths = []
    path = []  
    dfs(src, dest, graph, path, paths)
    return paths

if __name__ == "__main__":
    edges = [[0, 3], [0, 1], [1, 3], [2, 0], [2, 1]]
    src = 2
    dest = 3
    v = 4
    paths = find_paths(v, edges, src, dest)
    print(paths)
```
