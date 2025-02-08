# Backtracking

## Print all Unique Paths

- You can go either right or go down
- Source is 0,0
- Dest is m-1, n-1

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

## Subsets

[https://leetcode.com/problems/subsets/description/](https://leetcode.com/problems/subsets/description/)

$$ Time-Complexity: O(2^N) $$

```python
def subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    def helper(i, partial_ans):
        if i==len(nums):
            ans.append(partial_ans.copy())
            return

        # choose i
        partial_ans.append(nums[i])
        helper(i+1, partial_ans)
        partial_ans.pop()

        # not choose i
        helper(i+1, partial_ans)

    
    helper(0, [])
    return ans
```

## Subsets II

[https://leetcode.com/problems/subsets-ii/description/](https://leetcode.com/problems/subsets-ii/description/)

$$ Time-Complexity: O(2^N) $$

>Trick: Once you decide not to choose an element, never choose that element in future

```python
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    # sort so that duplicates are adjacent
    nums.sort()
    def helper(i, partial_ans):
        if i==len(nums):
            ans.append(partial_ans.copy())
            return

        # choose i
        partial_ans.append(nums[i])
        helper(i+1, partial_ans)
        partial_ans.pop()

        # not choose i
        # Don't choose nums[i], and also make sure you never choose it, hence we are skipping all the elements same as nums[i]
        while i<len(nums)-1 and nums[i]==nums[i+1]:
            i+=1
        helper(i+1, partial_ans)

    ans = []
    helper(0, [])
    return ans
```
