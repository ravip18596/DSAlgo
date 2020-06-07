You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

```text 
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```


`Solution`

```go
/**
Input
Amount - 5
Coins - [1,2,5]
**/
package main
import "fmt"

func change(amount int, coins []int) int {
    var dp []int
    dp = make([]int,amount+1)
    dp[0] = 1
    for i:=0;i<len(coins);i++{
        for j:=1;j<=amount;j++{
            if j>=coins[i]{
                dp[j] += dp[j-coins[i]]
            }
        }
        fmt.Println("combinations after coins ",coins[i]," are - ",dp)
        /**
        combinations after coins  1  are -  [1 1 1 1 1 1]
        combinations after coins  2  are -  [1 1 2 2 3 3]
        combinations after coins  5  are -  [1 1 2 2 3 4]
        **/
    }
    return dp[amount]
}
```

Question 2 - You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

```textExample 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
```
`Solution`

```go
package main
import "fmt"
/**
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
min ways for amount -  1 . dp -  [0 1 12 12 12 12 12 12 12 12 12 12]
min ways for amount -  2 . dp -  [0 1 1 12 12 12 12 12 12 12 12 12]
min ways for amount -  3 . dp -  [0 1 1 2 12 12 12 12 12 12 12 12]
min ways for amount -  4 . dp -  [0 1 1 2 2 12 12 12 12 12 12 12]
min ways for amount -  5 . dp -  [0 1 1 2 2 1 12 12 12 12 12 12]
min ways for amount -  6 . dp -  [0 1 1 2 2 1 2 12 12 12 12 12]
min ways for amount -  7 . dp -  [0 1 1 2 2 1 2 2 12 12 12 12]
min ways for amount -  8 . dp -  [0 1 1 2 2 1 2 2 3 12 12 12]
min ways for amount -  9 . dp -  [0 1 1 2 2 1 2 2 3 3 12 12]
min ways for amount -  10 . dp -  [0 1 1 2 2 1 2 2 3 3 2 12]
min ways for amount -  11 . dp -  [0 1 1 2 2 1 2 2 3 3 2 3]


**/
func coinChange(coins []int, amount int) int {
    dp := make([]int,amount+1)
    for i:=1;i<=amount;i++{
        dp[i] = amount+1
    }
    for i:=1;i<=amount;i++{
       for j:=0;j<len(coins);j++{
           if i>=coins[j]{
               dp[i] = min(dp[i],dp[i-coins[j]]+1)
           }
       }
        fmt.Println("min ways for amount - ",i,". dp - ",dp)
    }
    if dp[amount]<=amount{
        return dp[amount]
    }else{
        return -1
    }
}

func min(a,b int)int{
   if a<b{
 	return a
   }
   return b
}
```

`Question 3 - Perfect Squares`
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

```Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```
`Solutiom`

```go
package main
func numSquares(n int) int{
    intMax := int(1e10)

	dp := make([]int,n+1)
	for i:=0;i<=n;i++{
		dp[i]=intMax
	}
	dp[0]=0
	for i:=1;i<=n;i++{
		for j:=1;j*j<=i;j++{
			dp[i] = min(dp[i],dp[i- (j*j)]+1)
		}
	}
	return dp[n]
}

func min(a,b int)int{
	if a<b{
		return a
	}
	return b
}

```