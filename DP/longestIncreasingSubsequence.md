```text
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

```go
package main
func lengthOfLIS(nums []int) int {
    n := len(nums)
    if n==0{
        return 0
    }
    dp := make([]int,n)
    dp[0] = 1
    var ans int
    ans = 1
    var maxSequenceLen int
    for i:=1;i<n;i++{
        maxSequenceLen=0
        for j:=0;j<i;j++{
            if nums[i]>nums[j]{
                maxSequenceLen = max(maxSequenceLen,dp[j])
            }
        }
        dp[i] = maxSequenceLen + 1
        ans = max(ans,dp[i])
    }
    return ans
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```