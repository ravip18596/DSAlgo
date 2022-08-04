Solution
--------

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            curr = l1
            l1 = l1.next
        else:
            curr = l2
            l2 = l2.next
        pointer = curr

        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        if l1 is None:
            curr.next = l2
        else:
            curr.next = l1

        return pointer
```

### Golang

```golang
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil{
        return l2
    }
    if l2 == nil {
        return l1
    }
    var ptr, curr *ListNode
    if l1.Val < l2.Val{
        ptr = l1
        l1 = l1.Next
    }else{
        ptr = l2
        l2  = l2.Next
    }
    curr = ptr
    for l1 != nil && l2 != nil{
        if l1.Val < l2.Val{
            curr.Next = l1
            l1 = l1.Next
        }else{
            curr.Next = l2
            l2 = l2.Next
        }
        curr = curr.Next
    }
    if l1 == nil{
        curr.Next = l2
    }else{
        curr.Next = l1
    }
    return ptr
}
```
