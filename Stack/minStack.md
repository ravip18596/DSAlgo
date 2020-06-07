Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

`Solution`

```go
package main
import "fmt"
type MinStack struct {
    val []int
    min []int
}

/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{}
}


func (this *MinStack) Push(x int)  {
    this.val  = append(this.val,x)
    if len(this.min)==0{
        this.min = append(this.min,x)
    }else{
        this.min = append(this.min,minimum(x,this.min[len(this.min)-1]))
    }
}

func (this *MinStack) Pop()  {
    this.val = this.val[:len(this.val)-1]
    this.min = this.min[:len(this.min)-1]
}


func (this *MinStack) Top() int {
    return this.val[len(this.val)-1]
}


func (this *MinStack) GetMin() int {
    return this.min[len(this.val)-1]
}

func minimum(a,b int)int{
    if a<b{
        return a
    }
    return b
}


func main(){ 
 obj := Constructor()
 obj.Push(1)
 obj.Pop()
 param_3 := obj.Top()
 param_4 := obj.GetMin()
 fmt.Println(param_3,param_4)
}
```