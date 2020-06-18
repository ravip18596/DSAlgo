`Question`

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

```text
Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0

```

`Solution`

```go
package main
func searchInsert(arr []int, target int) int {
    var mid int
    var start,end = 0,len(arr)-1
    for start<=end{
        mid = (start+end)>>1
        if target > arr[mid]{
            start=mid+1
        }else if target < arr[mid]{
            end = mid-1
        }else{
            return mid
        }
    }
    return start
}
```
