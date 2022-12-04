54. Spiral Matrix

Solution
--------

- Time O(M^N)
```python
class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        i, j, rows, cols = 0, 0, len(m)-1, len(m[0])-1
        output = []

        while i<=rows and j<=cols:
            for k in range(j, cols+1):
                #print(m[i][k], i, k)
                output.append(m[i][k])
            i+=1
            for k in range(i, rows+1):
                #print(m[k][cols], i, k)
                output.append(m[k][cols])
            cols-=1
            
            if i<=rows:
                for k in range(cols,j-1,-1):
                    #print(m[rows][k], rows, k)
                    output.append(m[rows][k])
                rows-=1

            if j<=cols:
                for k in range(rows,i-1,-1):
                    #print(m[k][j], k, j)
                    output.append(m[k][j])
                j+=1

        return output
```
