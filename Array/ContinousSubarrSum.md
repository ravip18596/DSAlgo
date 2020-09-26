Problem
-------
```text
Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray 
of size at least 2 that sums up to a multiple of k.
```

Examples
--------
```text
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
```
Solution
---------
```text
the the difference is d between a and b, such as d = b - a(b is on the right of a). 
you want d is multiple of k, so you just need d % k = 0. 
Because d = b - a, so d % k = 0 = (b - a) %k. so (b-a)%k=0 equal b%k - a%k = 0, then b%k = a%k.
Time - O(N)
Space - O(N) 
```

```go
package main
/*
Corner cases :=
[0], 0 -> false;
[5, 2, 4], 5 -> false;
[0, 0], 100 -> true;
[1,5], -6 -> true;
*/
func checkSubarraySum(nums []int, k int) bool {
    n := len(nums)
    if n<2{
        return false
    }
    m := make(map[int]int)
    m[0]=-1
    var modSum int
    for i:=0;i<n;i++{
        modSum = modSum+nums[i]
        if k!=0{ modSum %= k }
        if _,ok:=m[modSum];!ok{
            m[modSum]=i
        }else{
            if i-m[modSum]>=2{
                return true
            }
        }
    }
    return false
}
```