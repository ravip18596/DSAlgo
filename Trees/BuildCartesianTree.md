```text
Given an inorder traversal of a cartesian tree, construct the tree.
Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 
```

`Solution - `

```go
package main
type TreeNode struct {
      Val int
      Left *TreeNode
      Right *TreeNode
}
func constructMaximumBinaryTree(A []int) *TreeNode {
    if len(A)==0{
        return nil
    }
    mi := max(A,0,len(A)-1)
    root := &TreeNode{Val:A[mi],Left:nil,Right:nil}
    root.Left = constructMaximumBinaryTree(A[:mi])
    root.Right = constructMaximumBinaryTree(A[mi+1:])
    return root
}
func max(arr []int,i,j int) int{
    mi := i
    for ;i<=j;i++{
        if arr[mi] < arr[i]{
            mi = i
        }
    }
    return mi
}
```