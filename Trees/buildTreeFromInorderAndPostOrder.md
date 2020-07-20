```text
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

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
func buildTree(inorder []int, postorder []int) *TreeNode {
    if len(inorder)==0 || len(postorder)==0{
        return nil
    }
    //since the last element of postorder is the root
    j:=len(postorder)-1
    i:=find(inorder,postorder[j])
    if i<0{
        return nil
    }
    root := &TreeNode{Val:postorder[j]}
    root.Left = buildTree(inorder[:i],postorder[:i])
    root.Right = buildTree(inorder[i+1:],postorder[i:j])
    return root
}

func find(arr []int,target int) int{
    for i:=0;i<len(arr);i++{
        if arr[i]==target{
            return i
        }
    }
    return -1
}
```