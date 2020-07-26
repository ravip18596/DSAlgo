
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

```text
If word1[i - 1] != word2[j - 1], we need to consider three cases.

    Replace word1[i - 1] by word2[j - 1] (dp[i][j] = dp[i - 1][j - 1] + 1);
    If word1[0..i - 1) = word2[0..j) then delete word1[i - 1] (dp[i][j] = dp[i - 1][j] + 1);
    If word1[0..i) + word2[j - 1] = word2[0..j) then insert word2[j - 1] to word1[0..i) (dp[i][j] = dp[i][j - 1] + 1).

```

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
    // since word1 = "" and to match word2
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

`Solution 2`

```go
package main
func minDistance(word1 string, word2 string) int {
    n,m:=len(word1),len(word2)
    dp := make([]int,m+1)
    prev := make([]int,m+1)
    for j:=1;j<=m;j++{
    	//base case
        prev[j] = j
    }
    for i:=1;i<=n;i++{
        dp[0] = i
        for j:=1;j<=m;j++{
            if word1[i-1]!=word2[j-1]{
                //dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                dp[j] = 1 + min(prev[j-1],prev[j],dp[j-1]) 
            }else{
                //dp[i][j] = dp[i-1][j-1]
                dp[j] = prev[j-1]  
            }
        }
        for i:=0;i<=m;i++{
            prev[i]=dp[i]   
        }
    }
    return prev[m]
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