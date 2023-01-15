# Problem

Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).

Input: grid = {{9,4,9,9},{6,7,6,4},
{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.

# Solution

- Consider matrix as graph and implement dijstra algorithm

```python
import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
	    def is_safe(i, j, V):
	        if i>=0 and j>=0 and i<V and j<V:
	            return True
	        return False
	        
		V = len(grid)
		inf = 0xffffffff
		pq = []
		dist = [[inf for _ in range(V)] for _ in range(V)]
		
		dist[0][0] = grid[0][0]
		heapq.heappush(pq, (dist[0][0], 0, 0))
		
		directions = [(-1,0), (0,1), (1,0),(0,-1)]
        while len(pq) > 0:
            _, i, j = heapq.heappop(pq)
            
            for k in range(4):
                _i,_j = i+directions[k][0],j+directions[k][1]
                
                if is_safe(_i,_j,V) and dist[_i][_j] > dist[i][j] + grid[_i][_j]:
                    dist[_i][_j] = dist[i][j] + grid[_i][_j]
                    heapq.heappush(pq, (dist[_i][_j], _i, _j))
        
        #print(dist)
        return dist[V-1][V-1]
```