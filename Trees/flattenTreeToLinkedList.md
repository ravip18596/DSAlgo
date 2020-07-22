```text
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

```

```go
package main
type TreeNode struct {
  Val int
  Left *TreeNode
  Right *TreeNode
}
//since flatening follows preorder traversal root->left->right
//we will build linked list in reverse form right<-left<-root
func flatten(root *TreeNode)  {
    var prev *TreeNode
    prev=nil
    util(root,&prev)
}

func util(root *TreeNode,prev **TreeNode) {
    if root==nil{
        return
    }
    util(root.Right,prev)
    util(root.Left,prev)
    root.Right=*prev
    root.Left = nil
    *prev = root
}
```