```text
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

```

`Recusive Solution`

```go
package main
type TreeNode struct {
      Val int
      Left *TreeNode
      Right *TreeNode
}
func isMirror(A,B *TreeNode) bool{
    if A==nil && B==nil{
        return true
    }
    if A==nil || B == nil{
        return false
    }
    return A.Val == B.Val && isMirror(A.Right,B.Left) && isMirror(A.Left,B.Right)
}

func isSymmetric(root *TreeNode) bool {
    return isMirror(root,root)
}
```

`Iterative Solution`