```text
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
```

```cgo
int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> maxheap;
    for(int i=0;i<stones.size();i++){
        maxheap.push(stones[i]);
    }
    int x,y;
    while(maxheap.size()>1){
        y = maxheap.top();
        maxheap.pop();
        x = maxheap.top();
        maxheap.pop();
        if(y>x){
            maxheap.push(y-x);
        }
    }
    if(maxheap.empty()){
        return 0;
    }else{
        return maxheap.top();
    }
}
```

```go
package main
import "container/heap"

type MaxHeap []int
func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Swap(i,j int) { h[i],h[j] = h[j],h[i] }
func (h MaxHeap) Less(i,j int) bool{ return h[i] > h[j] }

func (h *MaxHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{}{
    old := *h
    val := old[len(old)-1]
    old = old[:len(old)-1]
    *h = old
    return val
}
func lastStoneWeight(stones []int) int {
    pq := MaxHeap(stones)
    heap.Init(&pq)
    for pq.Len() > 1{
        y := heap.Pop(&pq).(int)
        x := heap.Pop(&pq).(int)
        if x<y{
            heap.Push(&pq,y-x)
        }
    }
    if pq.Len()==1{
        return heap.Pop(&pq).(int)
    }else{
        return 0
    }
}
```