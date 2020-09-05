Problem
-------
```text
A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible 
so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

Solution
---------

```text
For each letter encountered, process the last occurrence of that letter,
extending the current partition [start, end] appropriately.
```
```go
package main

func partitionLabels(S string) []int {
    lastOccurChar := make([]int,26,26)
    for index,c:=range S{
        lastOccurChar[c-'a']=index
    }
    var partitionSize []int 
    var start,end int
    for index,c:=range S{
        end = max(end,lastOccurChar[c-'a'])
        if index==end{
            partitionSize = append(partitionSize,end-start+1)
            start=index+1
        }
    }
    return partitionSize
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```