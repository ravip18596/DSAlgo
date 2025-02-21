# Linked List

## Find nth element in a Linked List

Given a linked list, write a function to find the nth element of the linked list.

```python
def nth_element(head, n):
    temp = head
    k = 1
    while temp is not None and k<n:
        temp = temp.next
        k+=1

    if temp is None:
        print("n > length, invalid n")
    else:
        print(f"Element at index {n} is {temp.val}")
```

## Deletion in Linked List

Given a linked list, write a function to delete a given node from the linked list.

```python
class LinkedList:
    def __init__(self, val, nexT=None):
        self.val = val
        self.next = nexT

def delete_node(head: LinkedList, node: int):
    # edge case
    if head.val == node:
        return head.next

    temp = head
    prev = None

    while temp is not None and temp.val != node:
        prev = temp
        temp = temp.next

    prev.next = temp.next

    return head
```

## Reverse a Linked List

> prev = pointer to starting node of already reversed linked list
> head = pointer to starting node of remaining linked list

```python
def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev
```

## Merge two sorted linked lists

```python
class Node:
    def __init__(self, val, nexT=None):
        self.val = val
        self.next = nexT


def merge(head1, head2):
    head = Node(-1)
    tail = head

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val < head2.val:
        tail.next = head1
        head1 = head1.next
        tail = tail.next
        tail.next = None
    else:
        tail.next = head2
        head2 = head2.next
        tail = tail.next
        tail.next = None

    if head1 is None:
        tail.next = head2
    else:
        tail.next = head1

    return head.next
```

## Linked List Cycle II

Return the node at the beginning of cycle

```python
class Node:
    def __init__(self, val, nexT=None):
        self.val = val
        self.next = nexT

    
def detectCycle(head):
    slow = head
    fast = head
    isCycle = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            isCycle = True
            break

    if not isCycle:
        return None

    slow2 = head
    while slow2 != slow:
        slow = slow.next
        slow2 = slow2.next

    return slow
```

## LRU Cache

1. using double linked list
2. using hash table

```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity       

    def get(self, key: int) -> int:
        # Case 1: if key is not present in cache, return -1
        if key not in self.cache:
            return -1
        else:
        # Case 2: If present, then return the value and move it to the end
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
        # Case 1: if cache is reached capacity then remove least recently used key
            if len(self.cache) == self.capacity:
                self.cache.popitem(0)
        else:
            self.cache.pop(key)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
