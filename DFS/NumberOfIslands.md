Problem
-------

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
```text
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Solution
--------
`Golang`
```go
package main
func dfs(grid [][]byte,xx,yy,rows,cols int) int{
    if xx<0 || xx>=rows || yy<0 || yy>=cols || grid[xx][yy]==byte('0'){
        return 0
    }
    grid[xx][yy] = byte('0')
    x := []int{0,1,0,-1}
    y := []int{1,0,-1,0}
    for k:=0;k<4;k++{
        newRow := xx+x[k]
        newCol := yy+y[k]
        dfs(grid,newRow,newCol,rows,cols)            
    }
    return 1 
}

func numIslands(grid [][]byte) int {
    rows := len(grid)
    if rows == 0{
        return 0
    }
    cols := len(grid[0])
    islands := 0
    for i:=0;i<rows;i++{
        for j:=0;j<cols;j++{
            islands += dfs(grid,i,j,rows,cols)    
        }
    }
    
    return islands
}
```

`Python`
```python
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        no_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    no_islands += self.dfs(grid,i,j,rows,cols)
                    
        return no_islands

    def dfs(self, grid: list[list[str]], i:int,j:int,rows:int,cols:int)->int:
        if i<0 or j<0 or i >= rows or j>=cols or grid[i][j]=="0":
            return 0
        grid[i][j] = "0"
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            self.dfs(grid,x,y,rows,cols)
            
        return 1
```