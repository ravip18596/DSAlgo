# Problem
complete the function printNearNodes() which takes the root Node of the BST and the range elements low and high as inputs and returns an array that contains the BST elements in the given range low to high (inclusive) in non-decreasing order.

Example 1:

Input:
       17
     /    \
    4     18
  /   \
 2     9 
l = 4, h = 24
Output: 4 9 17 18 

Example 2:

Input:
       16
     /    \
    7     20
  /   \
 1    10
l = 13, h = 23
Output: 16 20 

# Solution

```python
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #def util(root, low, high, array)
    def printNearNodes(self, root, low, high):
        #code here.
        if root is None:
            return []
        
        result = []
        result += self.printNearNodes(root.left, low, high)
        
        if root.data>=low and root.data<=high:
            result.append(root.data)
        
        result += self.printNearNodes(root.right, low, high)
            
        return result
```