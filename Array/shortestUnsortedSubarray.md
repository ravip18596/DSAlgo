```text
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

```

`Solution- Time - NlogN Space - O(N)`

```go
package main
import "sort"
func findUnsortedSubarray(nums []int) int {
    temp := make([]int,len(nums))
    copy(temp,nums)
    sort.Ints(temp)
    var minl,maxr int
    minl=len(nums)
    for i:=0;i<len(nums);i++{
        if nums[i]!=temp[i]{
            minl = min(minl,i)
            maxr = max(maxr,i)
        }
    }
    if minl==len(nums){
        return 0
    }
    return maxr-minl+1
}

func min(a,b int)int{
    if a<b{
        return a
    }
    return b
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```

`Solution - Time - O(N) and Space - O(N)`
```go
package main
func findUnsortedSubarray(nums []int) int {
    var stack []int
    maxr := 0
    minl := len(nums)
    //incresing 
    for i:=0;i<len(nums);i++{
        // if top of stack is greater than current then pop
        for len(stack)>0 && nums[stack[len(stack)-1]] > nums[i]{
            //pop and find the minimum index 
            minl = min(minl,stack[len(stack)-1])
            stack = stack[:len(stack)-1]
        }
        //push
        stack = append(stack,i)
    }
    stack = []int{}
    //decresing
    for i:=len(nums)-1;i>=0;i--{
        // if top of stack is less than current then pop
        for len(stack)>0 && nums[stack[len(stack)-1]] < nums[i]{
            maxr = max(maxr,stack[len(stack)-1])
            stack = stack[:len(stack)-1]
        }
        //push
        stack = append(stack,i)
    }
    if minl == len(nums){
        return 0
    }
    return maxr-minl+1
}

func min(a,b int)int{
    if a<b{
        return a
    }
    return b
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```