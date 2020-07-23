```text
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
![](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)
```text
Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

`Solution is using level order traversal. This solution is using queue`
```go
package main
type Node struct {
	Val int
    Left *Node
    Right *Node
	Next *Node
}
//similar to level order traversal
func connect(root *Node) *Node {
    if root==nil{
        return nil
    }
    queue := make([]*Node,0)
    queue = append(queue,root)
    queue = append(queue,nil)
    for len(queue)>0{
        front := queue[0]
        queue = queue[1:]
        if front==nil{
            if len(queue)>0{
                queue = append(queue,nil)
            }
        }else{
            front.Next = queue[0]
            if front.Left != nil{
                queue = append(queue,front.Left)
            }
            if front.Right != nil{
                queue = append(queue,front.Right)
            }
        }
    }
    return root
}
```