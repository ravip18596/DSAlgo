`Question`

Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

```text
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

```

`Solution`

![](https://assets.leetcode.com/static_assets/media/original_images/232_queue_using_stacksAPop.png)

```go
package main
type Stack struct{
    data []int
}

func StackConstruct() Stack{
    s := Stack{}
    s.data = make([]int,0)
    return s
}

func (this *Stack) Push(x int) {
    this.data = append([]int{x},this.data...)
}

func (this *Stack) Pop() int{
    val := this.data[0]
    this.data = this.data[1:]
    return val
}

func (this *Stack) IsEmpty() bool{
    return len(this.data) == 0
}

func (this *Stack) Top() int{
    return this.data[0]
}

type MyQueue struct {
    instack Stack
    outstack Stack
}


/** Initialize your data structure here. */
func Constructor() MyQueue {
    q := MyQueue{}
    q.instack = StackConstruct()
    q.outstack = StackConstruct()
    return q
}


/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int)  {
    this.instack.Push(x)
}


/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
    this.Peek()
    return this.outstack.Pop()
}


/** Get the front element. */
func (this *MyQueue) Peek() int {
    if this.outstack.IsEmpty(){
        for !this.instack.IsEmpty(){
            this.outstack.Push(this.instack.Pop())
        }
    }
    return this.outstack.Top()
}


/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
    return this.instack.IsEmpty() && this.outstack.IsEmpty()
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
```