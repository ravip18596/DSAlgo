# Dynamic Programming

## Fibonnaci number

>Recursive Solution

```python
def fib(n): 
    if n == 0:
        return 0
    if n == 1:  
        return 1            
    return fib(n-1) + fib(n-2)
```

> Memoization + Top-Down DP

```python
def fib(n):
    memo = {}
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in memo:
            return memo[n]
        memo[n] = helper(n-1) + helper(n-2)
        return memo[n]
    return helper(n)
```

> Tabulation + Bottom-Up DP

```python
def fib(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## LCS (Longest Common Subsequence)

$$ Time-Complexity: O(M*N) $$

>Tabulation + Bottom-Up DP
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[m][n]
```

>Memoization + Top-Down DP
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[-1] * (n+1) for _ in range(m+1)]
    def helper(i, j):
        if i == m or j == n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = helper(i+1, j+1) + 1
        else:
            dp[i][j] = max(helper(i+1, j), helper(i, j+1))
        return dp[i][j]
    return helper(0, 0)

def lcs2(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[-1] * (n+1) for _ in range(m+1)]
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = helper(i-1, j-1) + 1
        else:
            dp[i][j] = max(helper(i-1, j), helper(i, j-1))
        return dp[i][j]
    return helper(m, n)
```

## Longest Common Substring

$$ Time Complexity: O(n×m) $$
$$ Space Complexity: O(n×m) $$

```python
def longest_common_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    # Create a 2D array to store lengths of longest common suffixes
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    max_length = 0
    end_index = 0  # To store the end index of the longest common substring in str1
    
    # Build the dp array
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i  # Update the end index
            else:
                dp[i][j] = 0  # No common substring ends here
    
    # Extract the longest common substring
    if max_length == 0:
        return ""
    
    return str1[end_index - max_length:end_index]

# Example usage:
str1 = "abcdefgabcdegh"
str2 = "abcdeghabfvsnm"
print(longest_common_substring(str1, str2))  # Output: "abcdegh"
```
##  Longest Increasing Subsequence

```text
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Write your code here;
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            # we need to find the count of sequence at the end of s[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
```

## 0/1 Knapsack Problem

Pseudo Polynomial Time-Complexity: $O(N*W)$

> Tabulation + Bottom-Up DP
```python
def knapsack(W, wt, val, n):
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]
```

> Memoization + Top-Down DP
```python
def knapsack(W, wt, val, n):
    dp = [[-1] * (W+1) for _ in range(n+1)]
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + helper(i-1, j-wt[i-1]), helper(i-1, j))
        else:
            dp[i][j] = helper(i-1, j)
        return dp[i][j]
    return helper(n, W)
```

## Edit Distance

> Tabulation + Bottom-Up DP
```python
def editDistance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

> Memoization + Top-Down DP
```python
def editDistance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[-1] * (n+1) for _ in range(m+1)]
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i-1] == s2[j-1]:
            dp[i][j] = helper(i-1, j-1)
        else:
            dp[i][j] = 1 + min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1))
        return dp[i][j]
    return helper(m, n)
```

## LPS (Longest Palindromic Subsequence)

$$ Time-Complexity: O(N^2) $$

LPS(s1) => LCS(s1, reverse(s1))

> Tabulation + Bottom-Up DP
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[m][n]

def lps(s1):
    return lcs(s1, s1[::-1])
```

## Matrix Chain Multiplications

[https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1](https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1)

> Top-Down + Memoization

```python
def matrixMultiplication(self, arr):
    # code here
    n = len(arr)
    dp = [[-1]*(n-1) for _ in range(n-1)]
    
    def helper(arr, i, j, dp):
        if i==j:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        mini = int(1e9)+7
        for k in range(i, j):
            left_partition = helper(arr, i, k, dp)
            right_partition = helper(arr, k+1, j, dp)
            val = left_partition + right_partition + (arr[i]*arr[k+1]*arr[j+1])
            mini = min(mini, val)
            
        dp[i][j] = mini
        return mini
    
    return helper(arr, 0, n-2, dp)
```

## Best Time to Buy and Sell Stock

$$ Time-Complexity: O(N) $$
$$ Space-Complexity: O(N) $$

> Bottom-Up + Tabulation

```python
def maxProfit(prices):
    n = len(prices)
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = -prices[0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] - prices[i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + prices[i])
    return dp[1][n-1]
```

## Coin Change

$$ Time-Complexity: O(N*Amount) $$

> Bottom-Up + Tabulation

```python
def coinChange(coins, amount):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] += dp[j-coin]
    return dp[amount]

def coin_change(self, coins, amt):
    #Write your code here
    n = len(coins)
    dp = [[0]*(amt+1) for _ in range(n+1)]
     
    #   memo[i][j] = Number of ways you can make a coin change for j amount with coins from coins[i:end]
    #   Case 1 : You choose to have ith coin in your coin change, then total ways you can do it is memo[i][j-coins[i]]
    #   Case 2 : You decide not to choose the ith coin in your coin change, the total ways you can do it is memo[i+1][j]

    dp[n][0] = 1
    for j in range(amt+1):
      for i in range(n-1, -1, -1):
        dp[i][j] = dp[i+1][j]
        if j>=coins[i]:
          dp[i][j] += dp[i][j-coins[i]]

    return dp[0][amt]
```
