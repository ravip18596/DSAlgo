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

### Directed Graph

- Using DFS
- if we are able to get a visited node other than prev node from where I came from, as an adjacent node at any point of time during DFS, then there exists a cycle.

```python
def isDirectedGraphCyclic(node, graph, visited, prev):
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
            res = isDirectedGraphCyclic(i, graph, visited, prev)
            if res:
                print("Directe Graph is Cyclic")
                break
    if not res:
        print("Directe Graph is Acyclic")
```


### Undirected Graph
