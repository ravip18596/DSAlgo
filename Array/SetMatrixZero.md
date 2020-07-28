```text
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

`Solution - Time - O(N*N) Space - O(1)`

```go
package main
func setZeroes(m [][]int)  [][]int{
    r := len(m)
    if r == 0{
        return m
    }
    c,isCol := len(m[0]),false
    // Since first cell for both first row and first column is the same i.e. matrix[0][0]
    // We can use an additional variable for either the first row/column.
    // For this solution we are using an additional variable for the first column
    // and using matrix[0][0] for the first row.
    for i:=0;i<r;i++{
        if m[i][0]==0{
            isCol = true
        }
        for j:=1;j<c;j++{
            if m[i][j]==0{
                m[i][0] = 0
                m[0][j] = 0
            }
        }
    }
    
    for i:=1;i<r;i++{
        for j:=1;j<c;j++{
            if m[i][0]==0 || m[0][j]==0{
                m[i][j]=0
            }
        }
    }
    // See if the first row needs to be set to zero as well
    if m[0][0]==0{
        for j:=1;j<c;j++{
            m[0][j]=0
        }
    }
    // See if the first column needs to be set to zero as well
    if isCol{
        for i:=0;i<r;i++{
            m[i][0] = 0
        }
    }
    return m
}
```