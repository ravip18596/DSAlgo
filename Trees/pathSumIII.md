Brute Force
----------
### Space

- Space complexity is O(1), due to there is no extra cache. However, for any recursive question, we need to think about stack overflow, namely the recursion should not go too deep.
Assume we have n TreeNodes in total, the tree height will vary from O(n) (single sided tree) to O(logn)(balanced tree).
The two DFS will go as deep as the tree height.

### Time
Time complexity depends on the two DFS.
- 1st layer DFS will always take O(n), due to here we will take each node out, there are in total n TreeNodes
- 2nd layer DFS will take range from O(n) (single sided tree) to O(logn)(balanced tree). This is due to here we are get all the paths from a given node. The length of path is proportional to the tree height.
Therefore, the total time complexity is O(nlogn) to O(n^2).

```python
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, targetSum)->int:
            if root is None:
                return 0            
            res = 0
            if root.val == targetSum:
                res = 1
            res += dfs(root.left, targetSum-root.val)
            res += dfs(root.right, targetSum-root.val) 
            return res

        if root is None:
            return 0
    
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
```

Optimised Solution
------------------
```python
class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        self.dfs(root, target, 0, cache)
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
```



