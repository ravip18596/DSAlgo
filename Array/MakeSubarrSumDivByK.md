Problem
-------
```text
Given an array of positive integers nums,remove the smallest subarray
(possibly empty) such that the sum of the remaining elements is divisible by p. 
It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
```

Solution
--------
```text
we need that (sum(nums) - [subarray sum] )%p = 0
sum(nums)%p == subarrSum%p
sum(nums)%p == (Sum[0..i] - Sum[0..j<i])%p
Sum[0..j<i]%p = Sum[0..i]%p - sum(nums)%p

Time - O(N)
Space - O(N)
```
`Golang`
```go
package main
func minSubarray(nums []int, p int) int {
    n := len(nums)
    var prefixSum int
    for i:=0;i<n;i++{
        prefixSum += nums[i]
        prefixSum %= p
    }
    if prefixSum==0{
        return 0
    }
    hashMap := make(map[int]int)
    hashMap[0]=-1
    var curr,ans int
    ans = n
    for i:=0;i<n;i++{
        curr = (curr+nums[i])%p
        diff := (curr-prefixSum+p)%p
        if _,ok:=hashMap[diff];ok{
            ans = min(ans,i-hashMap[diff])
        }
        hashMap[curr]=i
    }
    if ans<n{
        return ans
    }
    return -1
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}
```
`Python`
```python3
def minSubarray(self, nums: List[int], p: int) -> int:
     arr_sum = sum(nums)
     rem = arr_sum%p
     if rem == 0:return 0 
     d = dict()
     d[0]=-1
     modSum,ans = 0,len(nums)
     for i in range(len(nums)):
         modSum = (modSum+nums[i])%p
         key = (modSum - rem)%p
         if key in d.keys():
             ans =  min(ans,i-d[key])
         d[modSum]=i
     
     return ans if ans<len(nums) else -1
```