```text
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

`Solution`

```go
package main
func canJump(nums []int) bool {
    n := len(nums)
    i,reach:=0,0
    for ;i<n && i<=reach;i++{
        reach = max(nums[i]+i,reach)
    }
    if i == n{
        return true
    }
    return false
}

func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}
```