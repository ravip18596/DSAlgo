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

```go
package main
type TreeNode struct {
      Val int
      Left *TreeNode
      Right *TreeNode
}
type Queue struct{
    arr []*TreeNode
}

func Constructor() Queue {
    q := Queue{}
    q.arr = make([]*TreeNode,0)
    return q
}

func (q *Queue) Enqueue(x *TreeNode) {
    q.arr = append(q.arr,x)
}

func (q *Queue) Dequeue() *TreeNode{
    temp := q.arr[0]
    q.arr = q.arr[1:]
    return temp
}

func (q *Queue) isEmpty() bool{
    return len(q.arr)==0
}
func isSymmetric(root *TreeNode) bool {
    q := Constructor()
    q.Enqueue(root)
    q.Enqueue(root)
    for !q.isEmpty(){
        t1 := q.Dequeue()
        t2 := q.Dequeue()
        if t1 == nil && t2 ==nil{
            continue
        }
        if t1 ==nil || t2 ==nil{
            return false
        }
        if t1.Val != t2.Val{
            return false
        }
        q.Enqueue(t1.Right)
        q.Enqueue(t2.Left)
        q.Enqueue(t1.Left)
        q.Enqueue(t2.Right)
    }
    return true
}
```