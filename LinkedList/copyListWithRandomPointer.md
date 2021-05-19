Problem
-------
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
- val: an integer representing Node.val 
- random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

`Example`
![Image](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

Solution
--------
![](https://raw.githubusercontent.com/hot13399/leetcode-graphic-answer/master/138.%20Copy%20List%20with%20Random%20Pointer.jpg)
`Python`
```python
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head 
        temp = head
        # self.print_nodes(head)
        # (7,None)->(13,7)->(11,1)->(10,11)->(1,7)->
        while temp != None:
            new_node = Node(x=temp.val)
            next_node = temp.next
            new_node.next = next_node
            temp.next = new_node
            temp = temp.next.next
            
        # self.print_nodes(head)
        #(7,None)->(7,None)->(13,7)->(13,None)->(11,1)->(11,None)->(10,11)->(10,None)->(1,7)->(1,None)->
        temp = head
        while temp != None:
            if temp.random is not None:
                random_node = temp.random
                temp.next.random = random_node.next
            temp = temp.next.next
        
        # self.print_nodes(head)
        # (7,None)->(7,None)->(13,7)->(13,7)->(11,1)->(11,1)->(10,11)->(10,11)->(1,7)->(1,7)->
        
        # Now split the list
        temp,clone_head = head, head.next
        temp2 = clone_head
        while temp2.next != None:
            temp.next = temp.next.next
            temp = temp.next
            
            temp2.next = temp2.next.next
            temp2 = temp2.next
        
        # self.print_nodes(clone_head)
        # (7,None)->(13,7)->(11,1)->(10,11)->(1,7)->
        return clone_head
        
    def print_nodes(self,head):
        temp = head
        while temp is not None:
            if temp.random is None:
                print(f"({temp.val},{temp.random})->",end='')
            else:
                print(f"({temp.val},{temp.random.val})->",end='')
            temp = temp.next
        
        print()
```        
`hash based solution`

`Golang`
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

`Python`
```python
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head 
        temp = head
        node_dict = {}
        while temp != None:
            node_dict[temp] = Node(x=temp.val,next=temp.next,random=temp.random)
            temp = temp.next
        
        temp = head
        while temp != None:
            if temp.next is not None:
                node_dict[temp].next = node_dict[temp.next]
            if temp.random is not None:
                node_dict[temp].random = node_dict[temp.random]
            
            temp = temp.next
        return node_dict[head]
```