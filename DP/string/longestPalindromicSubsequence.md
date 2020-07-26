```text
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2

One possible longest palindromic subsequence is "bb". 
```

`Solution`

```text
dp[i][j]: the longest palindromic subsequence's length of substring(i, j), here i, j represent left, right indexes in the string
State transition:
dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
Initialization: dp[i][i] = 1

ex - "cbbca"
[   
    [1 1 2 4 4]
    [0 1 2 2 2] 
    [0 0 1 1 1] 
    [0 0 0 1 1] 
    [0 0 0 0 1]
]
```

```go
package main
func longestPalindromeSubseq(s string) int {
    n := len(s)
    if n<=1{
        return n
    }
    if n==2{
        if s[0]==s[1]{
            return n
        }else{
            return 1
        }
    }
    dp := make([][]int,n)
    for i:=0;i<n;i++{
        dp[i] = make([]int,n)
        dp[i][i]=1
    }
    for i:=n-2;i>=0;i--{
        for j:=i+1;j<n;j++{
            if s[i]==s[j]{
                dp[i][j] = 2 + dp[i+1][j-1] 
            }else{
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
            }
        }
    }
    //fmt.Println(dp)
    return dp[0][n-1]
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```