# Graph

## DFS

> Depth First Search

$$Time-Complexity: O(V+E)$$

```python
def dfs(node, graph, visited):
    print(node)
    visited[node] = True    
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited)
    
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            dfs(i, graph, visited)
    print(visited)
```

## BFS

```python
def bfs(node, graph, visited):
    queue = [node]
    visited[node] = True
    while queue:
        node = queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            bfs(i, graph, visited)    
    print(visited)
```

## Bipartite Graph

Check whether a given graph is Bipartite or not

- Bipartite Graph
    - A graph where you can divide the vertices into two sets such that no edge connects two vertices of the same set.
    - Comes under application of BFS
    - real life example: transaction data between merchants and customers

- Using BFS
    - You will start with any node and mark it as blue
    - Mark all of its unvisited adjacent nodes as red
    - At any point of time, adjacent nodes of the same color, the graph is not Bipartite

```python
def isBipartiteGraph(graph):
    visited = [False] * len(graph)
    color = [0] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            color[i] = 1
            queue = [i]
            visited[i] = True
            while queue:
                node = queue.pop(0)
                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        color[neighbour] = 1 - color[node]
                        queue.append(neighbour)
                    else:
                        if color[neighbour] == color[node]:
                            return False
    return True
```

## Cycle Detection

Given a graph, find whether the graph contains a cycle or not.

### UnDirected Graph

- Using DFS
- if we are able to get a visited node other than prev node from where I came from, as an adjacent node at any point of time during DFS, then there exists a cycle.

```python
def isUnDirectedGraphCyclic(node, graph, visited, prev):
    visited[node] = True    
    for neighbour in graph[node]:
        if not visited[neighbour]:
            return isUnDirectedGraphCyclic(neighbour, graph, visited, node)
        else:
            if neighbour != prev:
                return True
    
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    visited = [False] * len(graph)
    prev = None
    res = False
    for i in range(len(graph)):
        if not visited[i]:
            res = isUnDirectedGraphCyclic(i, graph, visited, prev)
            if res:
                print("Directe Graph is Cyclic")
                break
    if not res:
        print("Directe Graph is Acyclic")
```


### Directed Graph

- Using DFS
- Visited
    - 0: unvisited
    - 1: visited node in the current recursion call
    - 2: visited node in the previous recursion call

```python
def isDirectedGraphCyclic(node, graph, visited):
    visited[node] = 1    
    for neighbour in graph[node]:
        if not visited[neighbour]:
            return isDirectedGraphCyclic(neighbour, graph, visited)
        else:
            if visited[neighbour] == 1:
                print("Graph is Cyclic")
                return
    
    visited[node] = 2
    
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    visited = [0] * len(graph)
    res = False
    isDirectedGraphCyclic(0, graph, visited)
```

## Topological Sort

- Topological Sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u->v, vertex u comes before v in the ordering.
- Topological Sort is possible only if the given graph is Acyclic.
- Topological Sort is not possible if the given graph is Cyclic.

```python
def dfs(node,graph,visited,stack):
    visited[node] = True
    for neighbour in graph[node]:    
        if not visited[neighbour]:
            dfs(neighbour,graph,visited,stack)
    stack.append(node)


def topologicalSort(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(i,graph,visited,stack)
    return stack
```

## Minimum Spanning Tree (MST)

- Minimum Spanning Tree is a subset of edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

- Using Prim's Algorithm

```python
def minimumSpanningTree(graph):
    num_vertices = len(graph)
    if num_vertices == 0:
        return []

    visited = [False] * num_vertices
    visited[0] = True
    mst = []
    edges = [] #store edges with weights

    for _ in range(num_vertices - 1):
        min_weight = float('inf')
        u, v = -1, -1

        for i in range(num_vertices):
            if visited[i]:
                for neighbor, weight in graph[i]:
                    if not visited[neighbor] and weight < min_weight:
                        min_weight = weight
                        u, v = i, neighbor

        if u != -1 and v != -1:
            visited[v] = True
            mst.append((u, v))
            edges.append((u,v,min_weight))
        else:
            # Graph might be disconnected
            break
    return edges
```

### Kruskal Algorithm

Steps -
1. Sort every edge in ascending order of weight.
2. Choose the minimum weighted edge as part of MST only if does'nt form a cycle.
3. After choosing V-1 edges, terminate the algorithm.

```python
def findrep(parent: List[int], u: int) -> int:
    if u == parent[u]:
        return u
    parent[u] = findrep(parent, parent[u])
    return parent[u]


def find(parent: List[int], u: int, v: int) -> bool:
    rep_u = findrep(parent, u)
    rep_v = findrep(parent, v)
    return rep_u == rep_v


def merge(parent: List[int], rank: List[int], u: int, v: int) -> None:
    rep_u = findrep(parent, u)
    rep_v = findrep(parent, v)
    if rep_u == rep_v:
        return
    if rank[rep_u] > rank[rep_v]:
        parent[rep_v] = rep_u
    elif rank[rep_u] < rank[rep_v]:
        parent[rep_u] = rep_v
    else:
        parent[rep_v] = rep_u
        rank[rep_u] += 1


def kruskalMST(graph):
    num_vertices = len(graph)
    if num_vertices == 0:
        return []

    edges = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = graph[i][j]
            if weight != 0:
                edges.append((i, j, weight))

    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices

    mst = []

    for u, v, weight in edges:
        same_set = find(parent, u, v)

        if not same_set:
            mst.append((u, v, weight))
            merge(parent, rank, u, v)

    return mst
```

## Dijsktra Algorithm (shortest path)

### Shortest distance from source node

```python
import heapq

class Solution:
    @staticmethod
    def dijkstra(n, graph, start):
      #Write your code here
      queue = [(0, start)]
      heapq.heapify(queue)
      dist = {}
      visited = [False for i in range(n)]
      for i in range(n):
        if i not in dist:
          dist[i] = 'Infinity'
      while len(queue)>0:
        node_dist, node = heapq.heappop(queue)
        if visited[node]:
          continue

        visited[node] = True
        dist[node] = node_dist
        for neigh_node, neigh_dist in graph[node]:
          if not visited[neigh_node]:
            new_dist = node_dist + neigh_dist
            heapq.heappush(queue, (new_dist, neigh_node))

      res = [f"{u} {v}" for u, v in dist.items()]
      return res
```

### Network Delay Time

[https://leetcode.com/problems/network-delay-time/description/](https://leetcode.com/problems/network-delay-time/description/)

```python
import heapq
import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        #print(f"graph is {graph}")
        
        time = dict()
        queue = []
        queue.append((0,k)) # keeping time as first tuple ele for heapify
        heapq.heapify(queue)
        while len(queue)>0:
            node_time,node = heapq.heappop(queue)
            if node in time.keys():
                # if already visited
                continue
            # mark node visited and store time
            time[node] = node_time
            for neigh_node,neigh_time in graph[node]:
                # check if neigh time is not visited.
                if neigh_node not in time.keys():
                    new_time = neigh_time + node_time
                    heapq.heappush(queue,(new_time,neigh_node))

        print(time)
        if len(time.keys()) != n:
            return -1
        return max(time.values())
```

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
