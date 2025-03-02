# Queue

## Circular Queue

Implement the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.


```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.head = -1
        self.tail = -1
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail+1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.queue[self.head] = -1
            self.head = -1
            self.tail = -1
            return True    

        self.queue[self.head] = -1
        self.head = (self.head+1) % self.size
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]


    def isEmpty(self) -> bool:
        return self.head == -1
        

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```
