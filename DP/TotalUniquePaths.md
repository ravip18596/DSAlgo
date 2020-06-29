`Problem`
```text
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
```
![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
`Solution`

```go
package main
func uniquePaths(m int, n int) int {
    dp := make([][]int,m)
    for i:=0;i<m;i++{
        dp[i] = make([]int,n)
        for j:=0;j<n;j++{
            dp[i][j]=1
        }
    }

    for i:=1;i<m;i++{
        for j:=1;j<n;j++{
            dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        }
    }
    return dp[m-1][n-1]
}

```

