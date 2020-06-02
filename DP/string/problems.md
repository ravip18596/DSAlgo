
`Question 1`

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

```Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

`Solution 1`

```go
package main
func minDistance(word1 string, word2 string) int {
    var m,n int
    if len(word1)<len(word2){
        word1,word2 = word2,word1
    }
    m,n = len(word1),len(word2)
    var dp [][]int
    dp = make([][]int,m+1)
    for i:=0;i<=m;i++{
        dp[i] = make([]int,n+1)
        //initialisation for base case.
        dp[i][0] = i
    }
    //initialisation for base case.
    for j:=1;j<=n;j++{
        dp[0][j] = j
    }
    
    for i:=1;i<=m;i++{
        for j:=1;j<=n;j++{
            if word1[i-1]!=word2[j-1]{
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
            }else{
                dp[i][j] = dp[i-1][j-1]
            }
        }
    }
    return dp[m][n]
}

func min(a ...int) int{
    mini := a[0]
    for i:=1;i<len(a);i++{
        if a[i]<mini{
            mini=a[i]
        }
    }
    return mini
}
```