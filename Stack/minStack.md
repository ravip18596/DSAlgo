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

O(1) get min operation

```python
def push(arr, ele):
    # Code here
    global minEle
    
    if len(arr)==0:
        # first insert
        minEle = ele
        arr.append(ele)
    else:
        if ele >= minEle:
            arr.append(ele)
        else:
            arr.append(2*minEle-ele)
            minEle=ele

# Function should pop an element from stack
def pop(arr):
    # Code here
    global minEle
    item = arr.pop()
    if item >= minEle:
        return item
    
    return 2*minEle-item

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return len(arr)==n

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return len(arr)==0

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    global minEle
    return minEle
```

# Get minimum element from stack

```python
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if len(self.s)==0:
            self.s.append(x)
            self.minEle = x
        elif x>=self.minEle:
            self.s.append(x)
        else:
            self.s.append(2*x - self.minEle)
            self.minEle = x

    def pop(self):
        #CODE HERE
        if len(self.s)==0:
            return -1
            
        top = self.s.pop()
        if top >= self.minEle:
            return top
        else:
            # very imp
            # if ele < minEle in stack, top is minEle
            top = self.minEle
            self.minEle = 2*self.minEle-top
            return top

    def getMin(self):
        #CODE HERE
        if len(self.s)==0 or self.minEle is None:
            return -1
            
        return self.minEle
```