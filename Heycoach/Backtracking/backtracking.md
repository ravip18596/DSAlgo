# Backtracking

## Print all Unique Paths

- You can go either right or go down
- Source is 0,0
- Dest is m-1, n-1

$$Time-Complexity 2^n $$

```python
def helper(i, j, grid, partial_ans):
    
    if i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 1:
        return

    if i==len(grid)-1 and j==len(grid[0])-1:
        print(partial_ans)
        return

    # go right
    partial_ans.append('R')
    helper(i, j+1, grid, partial_ans)
    # backtrack
    partial_ans.pop()

    # go down
    partial_ans.append('D')
    helper(i+1, j, grid, partial_ans)
    # backtrack
    partial_ans.pop()

grid = [[0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]]
helper(0, 0, grid, [])
```
