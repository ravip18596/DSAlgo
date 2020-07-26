```text
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

```

`Solution  Time - O(N) Space - O(N)`

```go
package main
func rob(nums []int) int {
    n := len(nums)
    if n==0{
        return 0
    }else if n==1{
        return nums[0]
    } 
    dp := make([]int,n)
    dp[0],dp[1] = nums[0],max(nums[0],nums[1])
    for i:=2;i<n;i++{
        notRob := dp[i-1]
        rob := dp[i-2]+nums[i]
        dp[i] = max(rob,notRob)
    }
    return dp[n-1]
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```

`Solution Time - O(N) Space - O(1)`

```go
func rob(nums []int) int {
    n := len(nums)
    if n==0{
        return 0
    }else if n==1{
        return nums[0]
    }
    dpi_2,dpi_1 := nums[0],max(nums[0],nums[1])
    maxL := dpi_1 // max(dp[i-1],dp[i-2]+nums[i])
    for i:=2;i<n;i++{
        maxL = max(dpi_1,dpi_2+nums[i])
        dpi_2 = dpi_1
        dpi_1 = maxL
    }
    return maxL
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```