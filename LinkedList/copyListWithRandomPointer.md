A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
![](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

`Solution`

```go
package main
type Node struct {
      Val int
      Next *Node
      Random *Node
 }

func copyRandomList(head *Node) *Node {
    m := make(map[*Node]*Node)
    var temp *Node
    temp = head
    for temp != nil{
        m[temp] = &Node{
            Val:temp.Val,
            Next:temp.Next,
            Random:temp.Random,
        }
        temp = temp.Next
    }
    temp = head
    for temp!=nil{
        if temp.Next != nil{
            m[temp].Next = m[temp.Next]
        }
        if temp.Random != nil{
            m[temp].Random = m[temp.Random]
        }
        temp = temp.Next
    }
    return m[head]
}
```