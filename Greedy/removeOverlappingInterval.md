```text
Given a collection of intervals, find the minimum number of intervals you need to remove 
to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```
`This problem is similar/almost identical to max meeting rooms problem`

`Solution - sort intervals by end time asc. and remove overlapping intervals`

`Time complexity - O(nlogn) and Space - O(n)`
```go
//this solution in case it is asked to return updated intervals
package main
import "sort"
type interval struct{
    start int
    end int
}

func eraseOverlapIntervals(intervals [][]int) int {
    if len(intervals)<=1{
        return 0
    }
    n := len(intervals)
    data := make([]interval,len(intervals))
    for i:=0;i<n;i++{
        data[i] = interval{start:intervals[i][0],end:intervals[i][1]}
    }
    sort.Slice(data,func(i,j int) bool{
        return data[i].end < data[j].end
    })
    for i:=1;i<len(data);{
        if data[i-1].end > data[i].start{
            //overlapping...so remove i 
            temp := data[:i]
            if i+1<len(data){
                data = append(temp,data[i+1:]...)
            }else{
                data = temp
            }
        }else{
            i++
        }
    }
    return n-len(data)
}
```

`Time - O(nlogn) Space - O(1)`

```go
package main
import "sort"
func eraseOverlapIntervals(intervals [][]int) int {
    if len(intervals)<=1{
        return 0
    }
    sort.Slice(intervals,func(i,j int) bool{
        return intervals[i][1] < intervals[j][1]
    })
    cnt := 0
    lastEnd := intervals[0][1]
    for i:=1;i<len(intervals);i++{
        if intervals[i][0] < lastEnd {
            //this interval i will be removed. so incr count
            cnt++
        }else{
            //this interval is good, so store its end time
            lastEnd = intervals[i][1]
        }
    }
    return cnt
}
```