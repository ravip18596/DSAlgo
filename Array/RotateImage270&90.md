Problem
-------
```text
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).
```

Solution
--------
```go
package main
func rotate(matrix [][]int)  {
    if len(matrix)==0 || len(matrix[0])==0{
        return
    }
    //reverse top to bottom
    i,j:=0,len(matrix)-1
    for i<j{
        matrix[i],matrix[j] = matrix[j],matrix[i]
        i++
        j--
    }
    //fmt.Println(matrix)
    for i:=0;i<len(matrix);i++{
        for j:=i+1;j<len(matrix[0]);j++{
            if i!=j{
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            }
        }
    }
}
```

```python
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Step 1 - Reverse the mat along the row
        n = len(matrix)
        i,j=0,n-1
        while i<j:
            matrix[i],matrix[j] = matrix[j],matrix[i]
            i,j=i+1,j-1
            
        #Step 2 - Reverse element across left diagonal or transpose   
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                       
```

# Problem

Rotate matrix 270* clockwise or 90 degree anticlockwise

# Solution
----------

1. Transpose
2. Swap row items column wise

```python
def rotate(matrix): 
    #code here
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
    # swap rows along columns
    for i in range(n//2):    
        for j in range(n):
            matrix[i][j],matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

    #or
    i,j = 0,n-1
    while i<j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        i,j = i+1,j-1
    
    return matrix
```