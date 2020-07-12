`Longest Palindromic Substring`

`Problem`
```text
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"


```

`Solution`

```go
package main
func longestPalindrome(s string) string {
    //using dp - dp[i][j] = s[i]==s[j] && dp[i+1][j-1]
    n := len(s)
    var dp [][]bool
    dp = make([][]bool,n)
    //base case - S(i,i) and S(i,i+1)
    for i:=0;i<n;i++{
        dp[i] = make([]bool,n)
        
    }
    
    var res string
    for i:=n-1;i>=0;i--{
        for j:=i;j<n;j++{
            dp[i][j] = s[i]==s[j] && (j-i<=2 || dp[i+1][j-1])
            if dp[i][j] && len(res) < j-i+1{
                res = s[i:j+1]
            }
        }
    }
    return res
}
```