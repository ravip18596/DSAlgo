```text
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

`Solution Time - O(N) Space - O(N)`
```go
package main
func climbStairs(n int) int {
    dp := make([]int,n+1)
    if n<=2{
        return n 
    }
    dp[1],dp[2] = 1,2
    for i:=3;i<=n;i++{
        dp[i] = dp[i-1]+dp[i-2]
    }
    return dp[n]
}
```
`Solution Time - O(N) Space - O(1)`
```go
package main
func climbStairs(n int) int {
    if n<=2{
        return n
    }
    count,c1,c2:=0,1,2
    for i:=3;i<=n;i++{
        count = c1+c2
        c1 = c2
        c2 = count
    }
    return count
}
````