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