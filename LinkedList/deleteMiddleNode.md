# Problem
Given a singly linked list, delete middle of the linked list. 
Complete the function deleteMid() which should delete the middle element from the linked list and return the head of the modified linked list.

Input:
LinkedList: 1->2->3->4->5
Output: 1 2 4 5

Input:
LinkedList: 1->2->3->4->5->6
Output: 1 2 3 5 6

# Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    slow, fast, prev = head, head, None
    while fast != None and fast.next != None:
        fast = fast.next.next
        prev=slow
        slow = slow.next
        
    prev.next = slow.next
    slow = None
    
    return head
```