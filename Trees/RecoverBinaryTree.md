```text
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

```
`Solution`

```go
package main
type TreeNode struct {
      Val int
      Left *TreeNode
      Right *TreeNode
}
/*
We need to find the first and second elements that are not in order right?

How do we find these two elements? For example, we have the following tree that is printed as in order traversal:

6, 3, 4, 5, 2

We compare each node with its next one and we can find out that 6 is the first element to swap because 6 > 3 and 2 is the second element to swap because 2 < 5.

Really, what we are comparing is the current node and its previous node in the "in order traversal".

*/
func recoverTree(root *TreeNode)  {
    var prevEle,firstEle,secondEle *TreeNode
    firstEle,secondEle = nil,nil
    INT_MIN := -1*int(1e10)
    prevEle = &TreeNode{Val:INT_MIN,Left:nil,Right:nil}
    traverse(root,&prevEle,&firstEle,&secondEle)
    if firstEle != nil && secondEle!= nil{
        firstEle.Val,secondEle.Val = secondEle.Val,firstEle.Val
    }
}

func traverse(root *TreeNode, prevEle,firstEle,secondEle **TreeNode) {
    if root==nil{
        return
    }
    traverse(root.Left,prevEle,firstEle,secondEle)
    //fmt.Println(root.Val,(*prevEle).Val,*firstEle,*secondEle)
    if *firstEle == nil && (*prevEle).Val >= root.Val{
        *firstEle = *prevEle    
    }
    if *firstEle != nil && (*prevEle).Val >= root.Val{
        *secondEle = root    
    }
    *prevEle = root
    traverse(root.Right,prevEle,firstEle,secondEle)
}
```