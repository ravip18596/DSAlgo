```text
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

```go
package main
func maxSubArray(nums []int) int {
    var cs,ls int
    cs = nums[0]
    ls = nums[0]
    for i:=1;i<len(nums);i++{
        if cs < 0{
            cs = nums[i]
        }else{
            cs += nums[i]
        }
        ls = max(ls,cs)
    }
    return ls
}

func max(i,j int) int{
    if i>j{
        return i
    }
    return j
}
```