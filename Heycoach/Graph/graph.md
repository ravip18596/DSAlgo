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
            return isDirectedGraphCyclic(neighbour, graph, visited, node)
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


### Undirected Graph

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
