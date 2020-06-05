
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Examples
```text
Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

```

```go
package main
type TreeNode struct {
 	Val int
 	Left *TreeNode
 	Right *TreeNode
}

func maxPath(root *TreeNode,maxi *int) int{
    if root==nil{
        return 0
    }
    left := max(0,maxPath(root.Left,maxi))
    right := max(0,maxPath(root.Right,maxi))
    *maxi =  max(left+right+root.Val,*maxi)
    return max(left,right)+root.Val
}
func maxPathSum(root *TreeNode) int {
    if root==nil{
        return 0
    }
    var maxi int =  -2147483648
    maxPath(root,&maxi)
    return maxi
}

func max(a... int) int{
    m := a[0]
    for i:=1;i<len(a);i++{
        if m < a[i]{
            m=a[i]
        }
    }
    return m
}
```