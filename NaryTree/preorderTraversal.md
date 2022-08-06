Problem
-------
[589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

Examples
--------
![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
- Input: root = [1,null,3,2,4,null,5,6]
- Output: [1,3,5,6,2,4]

Solution
--------

```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        nodes = [root.val]
        for i in range(0,len(root.children)):
            nodes += self.preorder(root.children[i])
        
        return nodes
```
