## Solution

preoder(Root->left->right)
ex,
```text
  1
 / \
2   3
   / \
  4   5 
```

return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
if you look at the return statement very closely, it is actually very intuitive
for value 1, you have 2 as left child and 3 as right child
for value 2, you have 'x'(None) as left child and 'x'(None) as right child which indicates it is a leaf node
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "x"
            
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == 'x':
            return None
        
        root = TreeNode(data[0])
        root.left = self.deserialize(data[1])
        root.right = self. deserialize(data[2])
        
        return root
```