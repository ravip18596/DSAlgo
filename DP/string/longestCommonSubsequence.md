```text
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 If there is no common subsequence, return 0.
Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

`Solution`

```go
package main
func longestCommonSubsequence(text1 string, text2 string) int {
    n1 := len(text1)
    n2 := len(text2)
    dp := make([][]int,n1+1)
    for i:=0;i<=n1;i++{
        dp[i] = make([]int,n2+1)
    }
    for i:=1;i<=n1;i++{
        for j:=1;j<=n2;j++{
            if text1[i-1]==text2[j-1]{
                dp[i][j] = dp[i-1][j-1] + 1
            }else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            }
        }
    }
    return dp[n1][n2]
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```