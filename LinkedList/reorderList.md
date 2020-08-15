```text
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

`Solution Time - O(n) Space - O(1)`

```go
package main

type ListNode struct {
	Val int
    Next *ListNode
}
// n = no of nodes in linked list
//Time Complexity - O(n/2) + O(n/2) + O(n) = O(n)  
//Space Complexity - O(1)
func reorderList(head *ListNode)  {
    if head == nil || head.Next == nil{
        return
    }
    // step 1. cut the list to two halves
    // prev will be the tail of 1st half
    // slow will be the head of 2nd half
    var prev *ListNode
    prev = nil
    slow,fast,l1 := head,head,head
    for fast != nil && fast.Next != nil{
        prev = slow
        slow = slow.Next
        fast = fast.Next.Next
    }
    prev.Next = nil
    // step 2. reverse the 2nd half
    l2 := reverse(slow)
    // step 3. merge two halves
    merge(l1,l2)
}

func reverse(head *ListNode) *ListNode{
    var prev,next *ListNode
    prev,next=nil,nil
    curr := head
    for curr != nil{
        next = curr.Next
        curr.Next = prev
        prev = curr
        curr = next
    }
    return prev
}

func merge(head1,head2 *ListNode){
    for head2!=nil{
        next := head1.Next
        head1.Next=head2
        head1 = head2
        head2 = next
    }
}
```