Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

![Cyclic Linked List](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

`Solution`

```go
package main
type ListNode struct {
   Val int
   Next *ListNode
 }
func detectCycle(head *ListNode) *ListNode {
    var slow,fast *ListNode 
    slow= head
    fast =head
    var isCycle = false
    for fast!=nil && fast.Next!=nil{
        
        slow = slow.Next
        fast = fast.Next.Next
        if slow==fast{
            isCycle = true
            break
        }
    }
    if !isCycle{
      return nil  
    } 
    slow2 := head
    for slow2!=slow {
        slow = slow.Next
        slow2 = slow2.Next
    }
    return slow
}
```