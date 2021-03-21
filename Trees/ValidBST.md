Problem
--------
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
Both the left and right subtrees must also be binary search trees.

Example
-------

```text
Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True
```
Solution
--------
`Golang`
```go
package main
type TreeNode struct {
 	Val int
 	Left *TreeNode
 	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
    return isValidBSTUtil(root,-int(1e10),int(1e10))
}

func isValidBSTUtil(root *TreeNode,mini,maxi int) bool{
    if root == nil{
        return true
    }
    leftSubTBst := isValidBSTUtil(root.Left,mini,root.Val)
    rightSubTBst := isValidBSTUtil(root.Right,root.Val,maxi)
    if leftSubTBst && rightSubTBst && root.Val>mini && root.Val<maxi{
        return true
    }
    return false
}
```
`Python`

```python
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right

class Solution:
    def isValidBST(self, root: TreeNode, mini=float('-inf'), maxi=float('inf')) -> bool:
        if root is None:
            return True
        
        left_bst = self.isValidBST(root.left,mini,root.val)
        right_bst = self.isValidBST(root.right,root.val,maxi)
        return left_bst and right_bst and root.val > mini and root.val < maxi
```