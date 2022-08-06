Problem
-------
[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Examples
--------
![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

- Input: 
  - root = [3,9,20,null,null,15,7]
- Output: 
  - [[3],[9,20],[15,7]]

Solution
--------
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        levels, level = [], []
        queue = [root, None]
        while len(queue)>0:
            front = queue[0]
            queue = queue[1:] # dequeue
            if front is None:
                levels.append(level)
                level = []
                if len(queue) > 0:
                    queue.append(None)
            else:
                level.append(front.val)
                if front.left is not None:
                    queue.append(front.left)
                
                if front.right is not None:
                    queue.append(front.right)
                    
                
        return levels
```
