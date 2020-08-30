Problem
--------
```text
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
```
Example
--------
```text
Input:
[[0,1,0,1,1],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]
 
Output:
[[0,1,0,1,2],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]
```
Solution
--------

`Time - O(N*N) Space-O(N*N)`

```go
package main
const inf = int(1e9)+7
func updateMatrix(matrix [][]int) [][]int {
    rows:=len(matrix)
    if rows==0{
        return matrix
    }
    cols := len(matrix[0])
    dp := make([][]int,rows)
    for i:=0;i<rows;i++{
        dp[i]=make([]int,cols)
        for j:=0;j<cols;j++{
            dp[i][j]=inf
        }
    }
    for i:=0;i<rows;i++{
        for j:=0;j<cols;j++{
            if matrix[i][j]==0{
                dp[i][j] = 0
            }else{
                //dp[i][j] = min(dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1)
                // minimum of the current dist and distance from top or left neighbour +1
                if i>0{
                    dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
                }
                if j>0{
                    dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
                }
            }
        }
    }
    for i:=rows-1;i>=0;i--{
        for j:=cols-1;j>=0;j--{
            //minimum of current dist and distances calculated from bottom and right neighbours
            //dp[i][j] = min(dp[i][j],dp[i+1][j]+1,dp[i][j+1]+1)
            if i<rows-1{
                dp[i][j] = min(dp[i][j],dp[i+1][j]+1)
            }
            if j<cols-1{
                dp[i][j] = min(dp[i][j],dp[i][j+1]+1)
            }
        }
    }
    return dp
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}
```