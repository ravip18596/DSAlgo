Problem
-------
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, 
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? 
If it is impossible, return -1.

Example
-------
![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)
```text
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
```

Solution
--------
```go
package main
import "container/heap"

type Node struct{
    val,time int
}
type minHeap []Node

func (n minHeap) Len() int {return len(n)}
func (n minHeap) Swap(i,j int) { n[i],n[j] = n[j],n[i] }
func (n minHeap) Less(i,j int) bool{ return n[i].time < n[j].time }
func (n *minHeap) Push(x interface{}) {
    *n = append(*n,x.(Node))
}
func (n *minHeap) Pop() interface{}{
    old := *n
    temp := old[len(old)-1]
    old = old[:len(old)-1]
    *n = old
    return temp
}
// heap based solution
// time - O(ElogE)
func networkDelayTime(times [][]int, N int, K int) int {
    //make adjacency matrix from edges
    adj := make([][]Node,N)
    for i:=0;i<len(times);i++{
        u,v,t := times[i][0],times[i][1],times[i][2]
        adj[u-1]=append(adj[u-1],Node{
            val:v,time:t,
        })
    }
    time := make(map[int]int)
    var queue minHeap
    queue = append(queue,Node{val:K,time:0})
    heap.Init(&queue)
    for queue.Len()>0{
        front := heap.Pop(&queue).(Node)
        //check if node is visited earlier then continue
        if _,ok:=time[front.val];ok{
            continue
        }
        //mark visited and store time
        time[front.val] = front.time
        for _,node:=range adj[front.val-1]{
            //check if neighbour time is not visited
            if _,ok:=time[node.val];!ok{
                node.time = front.time+node.time
                heap.Push(&queue,node)
            }
        }
    }
    
    //if visited map does not contain all the node key then it is not
    //possible for all nodes to receive signal
    if len(time)!=N{
        return -1
    }
    var ans int
    for _,val:=range time{
        ans = max(ans,val)
    }
    return ans
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```
```python
import heapq
import collections
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        #print(f"graph is {graph}")
        
        time = dict()
        queue = []
        queue.append((0,k)) # keeping time as first tuple ele for heapify
        heapq.heapify(queue)
        while len(queue)>0:
            node_time,node = heapq.heappop(queue)
            if node in time.keys():
                # if already visited
                continue
            # mark node visited and store time
            time[node] = node_time
            for neigh_node,neigh_time in graph[node]:
                # check if neigh time is not visited.
                if neigh_node not in time.keys():
                    new_time = neigh_time + node_time
                    heapq.heappush(queue,(new_time,neigh_node))

        print(time)
        if len(time.keys()) != n:
            return -1
        return max(time.values())
```

# BFS Solution

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            u, v, w = time
            graph[u].append((v, w))
            
        inf = float('inf')
        visit_time = [inf]*n
        queue = [(k,0)]
        
        while len(queue)>0:
            u, time = queue[0] // queue pop op
            queue = queue[1:] // deque op
            if time < visit_time[u-1]:
                visit_time[u-1] = time
                for v, w in graph[u]:
                    queue.append((v, time + w))
        
        ans = max(visit_time)
        return ans if ans < inf else -1
```