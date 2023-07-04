Problem
-------

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1



Solution
--------

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        dp = [[0]*n for _ in range(m)]  # dp[x][y] is the length of the maximal square at (x, y)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':  # ensure this condition first
                    # perform computation, mind border restrictions
                    dp[i][j] = min(dp[i-1][j] if i > 0 else 0,
                                   dp[i][j-1] if j > 0 else 0,
                                   dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                    if dp[i][j] > result:
                        result = dp[i][j]
        return result*result
```