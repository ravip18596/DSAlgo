# BFS (Breadth First Search)

## Shortest Path in Binary Matrix

```text
Given a square binary matrix, find the length of the shortest path from the top-left cell to the destination cell 
given as (x, y) moving only in up, down, left, right directions.
consider matrix as 0 indexed. You must return -1 in case of no path.
```

```text
Input
3 4
1 0 0 0 
1 1 0 1 
0 1 1 1
2 3
Output
5
Explanation:
we have to go from A[0][0] to A[2][3]. Minimun steps will be 5.
```

```python
class Solution:
    def shortestDistance(self, n, m, mat, x, y):
      # Check if the start or destination is blocked
      if mat[0][0] == 0 or mat[x][y] == 0:
        return -1

      # Directions for moving in the grid (right, down, left, up)
      directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

      # BFS initialization
      queue = [(0, 0, 0)]  # (row, col, distance)
      visited = set((0, 0))

      while queue:
        row, col, distance = queue.pop(0)
        # Check if we reached the destination
        if (row, col) == (x, y):
            return distance

        # Explore neighbors
        for dr, dc in directions:
          new_r, new_c = row+dr, col+dc
          if 0 <= new_r < n and 0<= new_c < m and (new_r, new_c) not in visited and mat[new_r][new_c] == 1:
            visited.add((new_r, new_c))
            queue.append((new_r, new_c, distance+1))
      
      return -1  


```

## Path Existence in an Undirected Graph

Return true if a route exists between the start and end nodes, otherwise return false.

```python
from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
      graph = defaultdict(list)
      for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

      queue = [source]
      visited = [False]*n

      while queue:
        node = queue.pop(0)
        visited[node] = True
        if node == destination:
          return True

        for neigh in graph[node]:
          if not visited[neigh]:
            queue.append(neigh)

      return False
```
