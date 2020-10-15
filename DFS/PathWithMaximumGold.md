Problem
-------
```text
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position you can walk one step to the left, right, up or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.
```

Examples
--------
```text
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
```

Solution
--------
```text
The idea is using backtracking to try all possible paths and return the path with maximum gold.
Complexity-Time: O(4 * 3^k), where k <= 25 is the number of cells that have gold.
Because the first cell has up to 4 choices, the (k-1) remain cells have up to 3 choices. 
And we make k different gold cells as first cell. 
So k * 4*3^(k-1) = 4 * 3^k
```
```go
package main
func getMaximumGold(grid [][]int) int {
    rows := len(grid)
    if rows==0{
        return 0
    }
    var maxGold int
    cols := len(grid[0])
    for i:=0;i<rows;i++{
        for j:=0;j<cols;j++{
            if grid[i][j]>0{
                maxGold = max(maxGold,dfs(grid,i,j,rows,cols))
            }
        }
    }
    return maxGold
}

func dfs(grid [][]int,i,j,rows,cols int) int{
    if !isSafe(grid,i,j,rows,cols){
        return 0
    }
    temp := grid[i][j]
    //mark visited
    var gold int
    grid[i][j] = -1
    xd := []int{0,1,0,-1}
    yd := []int{1,0,-1,0}
    for k:=0;k<4;k++{
        x := i+xd[k]
        y := j+yd[k]
        gold = max(gold,dfs(grid,x,y,rows,cols))
    }
    //unmark visited
    grid[i][j] = temp
    return temp + gold
}

func isSafe(grid [][]int,i,j,rows,cols int) bool{
    if i<0 || j<0 || i>=rows || j >= cols || grid[i][j]<=0{
        return false
    }
    return true
}
func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}
```

