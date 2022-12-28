## Problem
[https://www.geeksforgeeks.org/find-the-number-of-distinct-islands-in-a-2d-matrix/](https://www.geeksforgeeks.org/find-the-number-of-distinct-islands-in-a-2d-matrix/)

## Example
Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
Explanation:
grid[][] = {{1, 1, 0, 1, 1}, 
            {1, 0, 0, 0, 0}, 
            {0, 0, 0, 0, 1}, 
            {1, 1, 0, 1, 1}}
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.

## Solution

- Python

```python
def countDistinctIslands(self, grid : List[List[int]]) -> int:
    # code here        
    directions = [(-1,0), (0,1), (1,0),(0,-1)]
    def dfs(i,j,si,sj, result):
        if i<0 or j<0 or i>=r or j>=c or grid[i][j] <= 0:
            return
        
        result.append((i-si,j-sj))
        grid[i][j] = -1
        for d in directions:
            x, y = i+d[0], j+d[1]
            dfs(x,y, si,sj, result)
    
    islands = set()
    r,c = len(grid), len(grid[0])
    
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                result = []
                dfs(i,j, i, j, result)
                islands.add(tuple(result))
                
    return len(islands)
```

- Python
Optimised by removing set and tuple as set insert is log(n)

```python
def countDistinctIslands(self, grid : List[List[int]]) -> int:
    # code here
    directions = [(-1,0), (0,1), (1,0),(0,-1)]
    def dfs(i,j,si,sj):
        if i<0 or j<0 or i>=r or j>=c or grid[i][j] <= 0:
            return ""
        
        result = "{0}{1} ".format(i-si,j-sj)
        grid[i][j] = -1
        for d in directions:
            x, y = i+d[0], j+d[1]
            result += dfs(x,y, si,sj)
        
        return result
    
    islands = {}
    r,c = len(grid), len(grid[0]) 
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                result = dfs(i,j, i, j)
                #print(result)
                if result not in islands.keys():
                    islands[result] = 1
                
    #print(islands)
    return len(islands.keys())

- Java

```java
class Solution {
    // Function to find the number of islands.
    static int[][] dirs = {{-1,0},{0,1}, {1,0}, {0,-1}};

    private static void dfs(int[][] grid, int i, int j, int si, int sj, ArrayList<String> coords) {
        if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j] <= 0) {
            return;
        }
        grid[i][j] = -1;
        coords.add(Integer.toString(i-si) + " " + Integer.toString(j-sj));
        for(int k=0;k<4;k++)
        {
            dfs(grid, i+dirs[k][0], j+dirs[k][1], si, sj, coords);
        }
    }
    public int countDistinctIslands(int[][] grid) {
        // Code here
        HashSet<ArrayList<String>> islands = new HashSet<>();
        ArrayList<String> v;
        for(int i=0;i<grid.length;i++)
        {
            for(int j=0;j<grid[0].length;j++) {
                if(grid[i][j] == 1){
                    v = new ArrayList<>();
                    dfs(grid, i, j, i, j, v);
                    islands.add(v);
                }
            }
        }
        return islands.size();  
    }
}
```