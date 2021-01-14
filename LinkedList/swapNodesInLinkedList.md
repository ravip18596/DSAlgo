Problem
-------
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

### Examples
```text
Example 1
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```
![](https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg)

```text
Example 2
Input: head = [1], k = 1
Output: [1]
```

Solution
--------

`Golang`

```go
type ListNode struct {
    Val int
    Next *ListNode
}
 
func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}

func swapNodes(head *ListNode, k int) *ListNode {
    n := findLen(head)
    tmp := head
    first,sec := k,n-k+1
    // corner case
    if first == sec{
        return head
    }
    var firstNode,secNode *ListNode
    for i:=1;i<=max(first,sec);i++{
        if i==first{
            firstNode=tmp
        }else if i==sec{
            secNode=tmp
        }
        tmp = tmp.Next
    }
    // swap
    firstNode.Val,secNode.Val = secNode.Val, firstNode.Val
    return head
}

func findLen(head *ListNode) int {
    n := 0
    tmp := head
    for tmp != nil{
        n++
        tmp = tmp.Next
    }
    return n
}
```

`Python`

```python

```