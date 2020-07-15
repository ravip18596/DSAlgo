```text
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
Return true if and only if the nodes corresponding to the values x and y are cousins.
```
![](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)
```
Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```
![](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)
```
Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

![](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)
```
Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

`Solution`

```go
package main

type TreeNode struct {
	Val int
    Left *TreeNode
    Right *TreeNode
}
 
func util(root,parent *TreeNode,xparent,yparent **TreeNode,x,y,depth int,xdepth,ydepth *int) {
    if root==nil{
        return 
    }
    if root.Val==x{
        *xparent = parent
        *xdepth = depth
    }
    if root.Val==y{
        *yparent = parent
        *ydepth = depth
    }
    util(root.Left,root,xparent,yparent,x,y,depth+1,xdepth,ydepth)
    util(root.Right,root,xparent,yparent,x,y,depth+1,xdepth,ydepth)
}

func isCousins(root *TreeNode, x int, y int) bool {
    var xp,yp *TreeNode
    var xd,yd int
    xp = nil
    yp = nil
    xd=-1
    yd=-1
    util(root,nil,&xp,&yp,x,y,0,&xd,&yd)
    if xd!=-1 && yd != -1 && xp != nil && yp != nil{
        if xd==yd && *xp != *yp{
            return true
        }else{
            return false
        }
    }else{
        return false
    }
}
```