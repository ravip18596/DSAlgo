```text
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
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