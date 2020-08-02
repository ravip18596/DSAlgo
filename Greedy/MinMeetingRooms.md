```text
Given N lecture timings, with their start time and end time (both inclusive), the task is to find the minimum number of halls required to hold all the classes such that a single hall can be used for only one lecture at a given time. Note that the maximum end time can be 105.

Examples:

    Input: lectures[][] = {{0, 5}, {1, 2}, {1, 10}}
    Output: 3
    All lectures must be held in different halls because
    at time instance 1 all lectures are ongoing.

    Input: lectures[][] = {{0, 5}, {1, 2}, {6, 10}}
    Output: 2 
```

`Solution Approach`
```text
The idea is to maximise the no of lectures that are ongoing at a
particular instance of time
```

`Time - O(N) Space - (N)`
```go
package main
func solve(A [][]int )  (int) {
    var maxi int
    maxi = -1
    for i:=0;i<len(A);i++{
        maxi = max(maxi,A[i][1])
    }
    //fmt.Println(maxi)
    prefix := make([]int,maxi+2)
    for i:=0;i<len(A);i++{
        prefix[A[i][0]]+=1
        prefix[A[i][1]]-=1
    }
    //fmt.Println(prefix)
    maxi=prefix[0]
    for i:=1;i<len(prefix);i++{
        prefix[i]+=prefix[i-1]
        maxi = max(maxi,prefix[i])
    }
    //fmt.Println(prefix)
    return maxi
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```