```text
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
```
`Solution`

```go
package main
func majorityElement(nums []int) int {
    var maxi,maxv,n int
    maxi = 1
    maxv = nums[0]
    n = len(nums)
    for i:=1;i<n;i++{
        if maxv==nums[i]{
            maxi++
        }else{
            maxi--
            if maxi==0{
                maxi=1
                maxv=nums[i]
            }
        }
    }
    return maxv
}
```