Problem
----------

Solution
--------

## Solution 1 - Binary Indexed Tree (Segment Tree)

Segment Tree is based on the idea of storing partial sum.
When we try to calculate cumulative sum till any index n the steps that we follow are.

    Decompose n as the sum of power of 2's. Let's say n=n1+n2+...+nkn = n_{1} + n_{2} + ... + n_{k}n=n1​+n2​+...+nk​ where each of the number nin_{i}ni​ is a number which is a power of 2. For example, When n=7n = 7n=7, we have n1=1,n2=2,n3=4(7=1+2+4)n_{1} = 1, n_{2} = 2, n_{3} = 4 (7 = 1 + 2 + 4)n1​=1,n2​=2,n3​=4(7=1+2+4)

    The cumulative sum till index n in the nums array can then be obtained with the help of bit array as cum_sum(n)=bit[n1]+bit[n2]+...+bit[nk]cum\_sum(n) = bit[n_{1}] + bit[n_{2}] + ... + bit[n_{k}]cum_sum(n)=bit[n1​]+bit[n2​]+...+bit[nk​]


## Solution 2 - Brute Force Solution

### Complexity Analysis

- Time Complexity
    - sumRegion - O(MN) per query.
    - update - O(1)O(1)O(1) per query.

- Space Complexity: O(1)

```go
type NumMatrix struct {
    matrix [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    return NumMatrix{
        matrix: matrix,
    }
}


func (this *NumMatrix) Update(row int, col int, val int)  {
    rows,cols := len(this.matrix),0
    if rows>0{
        cols = len(this.matrix[0])
    }
    if row<0 || col<0 || row>=rows || col>cols{
        return
    }
    this.matrix[row][col] = val
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    var sum int
    for i:=row1;i<=row2;i++{
        for j:=col1;j<=col2;j++{
            sum += this.matrix[i][j]
        }
    }
    return sum
}
```
