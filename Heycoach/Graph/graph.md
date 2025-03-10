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
