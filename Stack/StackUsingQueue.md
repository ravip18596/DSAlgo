`Question`
Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

```text
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

`Solution`

![](https://assets.leetcode.com/static_assets/media/original_images/225_stack_using_queues_pushC.png)

```go
package main
type Queue struct{
    data []int
}

func QueueConstruct() Queue{
    q := Queue{}
    q.data = make([]int,0)
    return q
}

func (this *Queue) Enqueue(x int){
    this.data = append(this.data,x)
}

func (this *Queue) Front() int{
    return this.data[0]
}

func (this *Queue) Dequeue() int{
    val := this.data[0]
    this.data = this.data[1:]
    return val
}

func (this *Queue) IsEmpty() bool{
    return len(this.data)==0
}
type MyStack struct {
    q Queue
}


/** Initialize your data structure here. */
func Constructor() MyStack {
    s := MyStack{}
    s.q = QueueConstruct()
    return s
}


/** Push element x onto stack. */
func (this *MyStack) Push(x int)  {
    this.q.Enqueue(x)
    for i:=0;i<len(this.q.data)-1;i++{
        this.q.Enqueue(this.q.Dequeue())
    }
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
    return this.q.Dequeue()
}


/** Get the top element. */
func (this *MyStack) Top() int {
    return this.q.Front()
}


/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
    return this.q.IsEmpty()
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
```

