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
from collections import defaultdict

class Solution:
	def dfs(self, node, graph, visited, prev):
	    visited[node] = True
	    for neigh in graph[node]:
	        if not visited[neigh]:
	            if self.dfs(neigh, graph, visited, node):
	                return True
	        else:
	            if neigh!=prev:
	                return True
	                
	    return False
	            
	    
	def isCycle(self, V, edges):
		#Code here
		graph = defaultdict(list)
		for u,v in edges:
		    graph[u].append(v)
		    graph[v].append(u)
		    
		visited = [False]*V
		prev = None
		for i in range(V):
		    if not visited[i]:
		        if self.dfs(i, graph, visited, prev):
		            return True
		            
		return False
```


### Directed Graph

- Using DFS
- Visited
    - 0: unvisited
    - 1: visited node in the current recursion call
    - 2: visited node in the previous recursion call

```python
def isDirectedGraphCyclic(node, graph, visited):
    if visited[node]==2:
        return False
    if visited[node]==1:
        return True
    visited[node] = 1    
    for neighbour in graph[node]:
        if isDirectedGraphCyclic(neighbour, graph, visited):
            return True

    visited[node] = 2
    return False
    
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    visited = [0] * len(graph)
    for i in range(n):
        if visited[i]==0:
            if isDirectedGraphCyclic(i, graph, visited):
                return True
    
    return False
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

### Prim MST on undirected graph using priority queue
- Time Complexity - O((E+V)*log(V))
- Space Complexity - O(E+V)

```python
from collections import defaultdict
import heapq

class Solution:
    def spanningTree(self, V, edges):
        # code here
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        visited = [False]*V
        pq = []
        total_wt = 0
        # starting with vertex 0
        heapq.heappush(pq, (0, 0)) # (weight, vertex_no)
        while pq:
            wt, u = heapq.heappop(pq)
            if visited[u]:
                continue
                # Skip if already visited
            total_wt += wt
            visited[u] = True
            for neigh, w in graph[u]:
                if not visited[neigh]:
                    heapq.heappush(pq, (w, neigh))
                        
        return total_wt
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

## Star Graph

```text
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
```

Solution
```python
class Solution:
    def find_center(self, edges):
      from collections import defaultdict

      graph = defaultdict(list)
      indegree = {}
      for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        indegree[u] = indegree.get(u, 0) + 1
        indegree[v] = indegree.get(v, 0) + 1

      n = len(indegree)
      for node, val in indegree.items():
        if val == n-1:
          return node
      return -1
```

## identify all the critical connections in a network of servers

Sample Input:
```text
7 8
6 1
4 2
2 5
1 5
0 1
1 2
2 0
1 3
```text
Sample Output:
```text
1 6
2 4
1 3
Constraints:
2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= ai, bi <= n - 1
ai != bi
Connections are unique and undirected.
Explanation: In this example, the network consists of 7 servers and 8 connections. The critical connections are between servers 1-6, 2-4, and 1-3. Removing any of these connections would result in at least one server being isolated from the rest of the network.
```

- we can use a depth-first search (DFS) approach.
- The idea is to find bridges in the graph, which are edges that, when removed, increase the number of connected components in the graph.

Here's a step-by-step explanation of how to implement this:

- Graph Representation: Use an adjacency list to represent the graph.
- DFS Traversal: Perform a DFS traversal to explore the graph. During the traversal, maintain discovery and low values for each node:
  - discovery[u]: The time when node u is visited.
  - low[u]: The lowest discovery time reachable from node u.
- Bridge Condition: For each edge (u, v), if low[v] > discovery[u], then (u, v) is a critical connection (bridge).
- Backtracking: Update the low values during the DFS backtracking phase.
- Output: Collect all the critical connections and print them.

```python
def criticalConnections(n, connections):
    from collections import defaultdict

    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize variables for DFS
    discovery = [-1] * n
    low = [-1] * n
    bridges = []
    time = [0]  # Use a list to keep track of time as a mutable object

    def dfs(u, parent):
        discovery[u] = low[u] = time[0]
        time[0] += 1

        for v in graph[u]:
            if v == parent:  # Ignore the edge back to the parent
                continue
            if discovery[v] == -1:  # If v is not visited
                dfs(v, u)
                low[u] = min(low[u], low[v])  # Update low value

                # Check if the edge (u, v) is a bridge
                if low[v] > discovery[u]:
                    bridges.append((u, v))
            else:  # If v is already visited
                low[u] = min(low[u], discovery[v])  # Update low value

    # Start DFS from each unvisited node
    for i in range(n):
        if discovery[i] == -1:
            dfs(i, -1)

    return bridges

# Sample Input
n = 7
connections = [
    [6, 1],
    [4, 2],
    [2, 5],
    [1, 5],
    [0, 1],
    [1, 2],
    [2, 0],
    [1, 3]
]

# Get critical connections
result = criticalConnections(n, connections)

# Print the result
for u, v in result:
    print(u, v)
```
