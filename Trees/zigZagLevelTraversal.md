```text
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
```

```go
package main
type TreeNode struct{
	Val int
	Left *TreeNode
	Right *TreeNode
}
func zigzagLevelOrder(root *TreeNode) [][]int {
    m := make(map[int][]int)
    util(root,0,m)
    result := make([][]int,len(m))
    for key,val:=range m{
        if key%2!=0{
            for i,j:=0,len(val)-1;i<j;i,j=i+1,j-1{
                val[i],val[j] = val[j],val[i]
            }
        }
        result[key] = val
    }
    return result
}

func util(root *TreeNode,level int,m map[int][]int) {
    if root == nil{
        return 
    }
    m[level] = append(m[level],root.Val)
    util(root.Left,level+1,m)
    util(root.Right,level+1,m)
}

```