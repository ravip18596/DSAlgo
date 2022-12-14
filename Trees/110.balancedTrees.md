```text
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

```

```go
package main
type TreeNode struct {
 	Val int
 	Left *TreeNode
 	Right *TreeNode
}
func isBalanced(root *TreeNode) bool {
    _,bal:=treeUtil(root)
    return bal
}

func treeUtil(root *TreeNode) (int,bool){
    if root==nil{
        return 0,true
    }
    ld,balLeft := treeUtil(root.Left)
    rd,balRight := treeUtil(root.Right)
    height := max(ld,rd)+1
    if balLeft && balRight && abs(ld-rd)<=1{
        return height,true
    }
    return height,false
}

func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}

func abs(a int) int{
    if a<0{
        return -1*a
    }
    return a
}
```