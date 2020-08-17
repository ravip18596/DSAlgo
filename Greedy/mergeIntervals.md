```text
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

`Time Complexity - O(nlogn) Space - O(1) becoz inplace modifications`

```go
package main
import "sort"
func merge(intervals [][]int) [][]int {
    if len(intervals) <= 1{
        return intervals
    }
    sort.Slice(intervals,func(i,j int) bool{
        return intervals[i][0] < intervals[j][0]
    })
    var temp1,temp2 [][]int
    for i:=1;i<len(intervals);{
        if intervals[i][0] <= intervals[i-1][1] {
            //merge intervals i-1,i into i-1
            intervals[i-1][0] = intervals[i-1][0]
            intervals[i-1][1] = max(intervals[i][1],intervals[i-1][1])
            //remove interval i
            temp1 = intervals[:i]
            if i+1<len(intervals){
                temp2 = intervals[i+1:]
                intervals = append(temp1,temp2...)
            }else{
                intervals = temp1
            }    
        }else{
            i++
        }
    }
    return intervals
}


func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}
```