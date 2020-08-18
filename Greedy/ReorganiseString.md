```text
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""
```

`Solution 1 - Using Priority Queue`
```go
package main
import "container/heap"

type CharFreq struct{
    Char rune
    Count int
}
type priorityQueue []*CharFreq

func (h priorityQueue) Less(i,j int) bool{ return h[i].Count > h[j].Count }
func (h priorityQueue) Len() int { return len(h) }
func (h priorityQueue) Swap(i,j int) { h[i],h[j] = h[j],h[i] }

func (h *priorityQueue) Push(x interface{}) {
    *h = append(*h,x.(*CharFreq))
}

func (h *priorityQueue) Pop() interface{} {
    old := *h
    popEle := old[len(old)-1]
    old = old[:len(old)-1]
    *h = old
    return popEle
}

func reorganizeString(S string) string {
    freqMap := make(map[rune]*CharFreq)
    for _,c:=range S{
        if _,ok:=freqMap[c-97];!ok{
            freqMap[c-97] = &CharFreq{Count:1,Char:c}
        }else{
            freqMap[c-97].Count += 1
            freqMap[c-97].Char = c
            //task is only impossible if the frequency of a letter exceeds (N+1) /2
            if freqMap[c-97].Count > (len(S)+1)/2{
                return ""
            }
        }
    }
    freqHeap := make(priorityQueue,0)
    for _,val:=range freqMap{
        freqHeap = append(freqHeap,val)
    }
    var result []rune
    heap.Init(&freqHeap) //This is O(N)
    for freqHeap.Len()>=2{
        top1 := heap.Pop(&freqHeap).(*CharFreq)
        result = append(result,top1.Char)
        top2 := heap.Pop(&freqHeap).(*CharFreq)
        result = append(result,top2.Char)
        top1.Count-=1
        top2.Count-=1
        if top1.Count>0{ heap.Push(&freqHeap,top1) }
        if top2.Count>0{ heap.Push(&freqHeap,top2) }
    }
    for freqHeap.Len()>0{
        top := heap.Pop(&freqHeap).(*CharFreq)
        result = append(result,top.Char)
    }
    return string(result)
}
```