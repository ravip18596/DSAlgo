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
