```text
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```

```go
package main
type TreeNode struct {
 	Val int
 	Left *TreeNode
 	Right *TreeNode
}
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder)==0 || len(inorder)==0{
        return nil
    }
    i:= find(inorder,preorder[0])
    if i<0{
        return nil
    }
    root := &TreeNode{Val:preorder[0]}
    root.Left = buildTree(preorder[1:i+1],inorder[:i])
    root.Right = buildTree(preorder[i+1:],inorder[i+1:])
    return root
}

func find(arr []int,target int) int{
    for i,v := range arr{
        if v==target{
            return i
        }
    }
    return -1
}
```