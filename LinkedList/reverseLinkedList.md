Solution
--------

### Python

```python

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            # base case of 0 or 1 node
            return head
        
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
```
- Time Complexity - O(N)
- Space Complexity - O(1)

## Python
### Iterative

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
```
### Recursive
- Time Complexity - O(N)
- Space Complexity - O(1)

```python

```

