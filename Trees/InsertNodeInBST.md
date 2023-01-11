Problem
-------
```text
Given the root node of a binary search tree (BST) and a value
to be inserted into the tree, insert the value into the BST.
Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.
```
Example
-------
```text
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
```
```text
         4
       /   \
      2     7
     / \   /
    1   3 5
```

Solution
--------
```text
Time - O(N)
Space - O(N) //recursive space
```

```go
package main
type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}
 
func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root==nil{
        t := TreeNode{Val:val,Left:nil,Right:nil}
        return &t
    }
    if root.Val>val{
        //left subtree
        root.Left = insertIntoBST(root.Left,val)
    }else{
        root.Right = insertIntoBST(root.Right,val)
    }
    return root
}
```

Slight Variation
> Note: If K is already present in the BST, don't modify the BST.

```python
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def insert(root, Key):
    # code here
    if root is None:
        return Node(Key)
        
    # if matching then return existing root.
    if root.data == Key:
        return root
        
    if root.data > Key:
        # left
        root.left = insert(root.left, Key)
    else:
        # right
        root.right = insert(root.right, Key)
        
    return root
```