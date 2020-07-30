Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

```
Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
```

`Solution`

```go
package main
type ListNode struct {
	Val int
	Next *ListNode
}
 
func reverseKGroup(head *ListNode, k int) *ListNode {
    var curr *ListNode
    curr = head
    count := 0
    for(curr != nil && count != k){
        curr = curr.Next
        count++
    }
    if (count == k) {
        curr = reverseKGroup(curr,k)
        for(count>0){
            temp := head.Next
            head.Next = curr
            curr = head
            head = temp
            count--
        }
        head = curr
    }
    return head
}
```