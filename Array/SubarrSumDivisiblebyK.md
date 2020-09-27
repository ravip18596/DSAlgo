Problem
---------
```text
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```


Solution
--------
```text
if sum[0, i] % K == sum[0, j] % K, sum[i + 1, j] is divisible by by K.
So for current index j, we need to find out how many index i (i < j) exit that has the same mod of K.
Time - O(N)
Space - O(K)
```

```go
package main
func subarraysDivByK(A []int, K int) int {
    m := make([]int,K)
    //zero sum cnt
    m[0] = 1 //remainder = 0  - base case
    var sum int
    for i:=0;i<len(A);i++{
        sum = (sum+A[i])%K //if sum A[i:j] = sum A[0:j] - sum[0:i-1] has the same remainder
        if sum<0{
            sum += K   // in case sum is -1 add K i.e -1%5 = -1+5 = 4 
        }
        m[sum]+=1
    }
    //counting pairs => N choose 2 = > nC2 => n*(n-1) / 2.
    var ans int
    for _,cnt:=range m{
        ans += ((cnt-1)*cnt)>>1
    }
    return ans
}
```