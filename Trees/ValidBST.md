```text
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    Both the left and right subtrees must also be binary search trees.

Example :

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
`Solution`

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