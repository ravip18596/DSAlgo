Backtracking algo
-----------------
`We can consider backtracking as a state machine`
![](https://leetcode.com/problems/unique-paths-iii/Figures/980/980_state_machine.png)
```text
    def backtrack(cell):
        1. if we arrive at the final state:
             path_count ++
             return

        2. mark the current cell as visited

        3. for next_cell in 4 directions:
             if next_cell is not visited and non-obstacle:
                 backtrack(next_cell)

        4. unmark the current cell
```

Problem
-------
```text
On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.
```

Examples
--------
```text
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
```

Solution
--------
```text
Time Complexity: O(3^N)
Although technically we have 4 directions to explore at each step, 
we have at most 3 directions to try at any moment except the first step.
The last direction is the direction where we came from,
therefore we don't need to explore it, since we have been there before.

Space Complexity: O(N)
This is largely recursive space
```
```go
package main
func uniquePathsIII(grid [][]int) int {
    var paths int
    rows := len(grid)
    if rows==0{
        return paths
    }
    cols := len(grid[0])
    var startRow,startCol,nonObstacles int
    for i:=0;i<rows;i++{
        for j:=0;j<cols;j++{
            if grid[i][j]==1{
                startRow = i
                startCol = j
            }
            if grid[i][j]>=0{
                nonObstacles++
            }
        }
    }
    dfs(grid,&paths,startRow,startCol,nonObstacles)
    return paths
}

func dfs(grid [][]int,pathcnt *int,i,j,nonObstacles int){
    if grid[i][j]==2 && nonObstacles==1{
        //1. ending cell - final state
        *pathcnt++
        return
    }
    //2. mark cell visited
    temp := grid[i][j]
    grid[i][j]=-4
    //3. visit neighbouring cells
    xarr := []int{1,0,0,-1}
    yarr := []int{0,1,-1,0}
    for k:=0;k<4;k++{
        x := i+xarr[k]
        y := j+yarr[k]
        if isSafe(x,y,len(grid),len(grid[0])) && grid[x][y]>=0{
            dfs(grid,pathcnt,x,y,nonObstacles-1)
        }
    }
    //4. unmark the current cell
    grid[i][j]=temp
}

func isSafe(i,j,rows,cols int) bool{
    if i<0 || j<0 || i>=rows || j>=cols{
        return false
    }
    return true
}
```