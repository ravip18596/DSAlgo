# Sliding Window

## Minimum Size Subarray Sum

>Problem Statement - [https://leetcode.com/problems/minimum-size-subarray-sum/description/](https://leetcode.com/problems/minimum-size-subarray-sum/description/)


- Java

```java
public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int n = nums.length;
        
        int left=0,sum=0;
        int maxi = Integer.MAX_VALUE;
        for(int i=0;i<n;i++){
            sum+=nums[i];
            while(sum>=s){
                maxi = Math.min(maxi,i-left+1);
                sum-=nums[left++];
            }
        }
        return maxi==Integer.MAX_VALUE?0:maxi;
    }
}
```

## Maximum Sum of Almost Unique Subarray

>Problem Statement [https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/)


- Go

```go
func maxSum(nums []int, a int, k int) int64 {
    m := make(map[int]int)
    var sum, maxSum int64
    for i:=0;i<k;i++{
        sum += int64(nums[i])
        m[nums[i]]++
    }
    if len(m) >= a{
        maxSum = sum
    }
    i, j, n := k, 0, len(nums)
    for i<n{
        num, prev_num := nums[i], nums[j]
        i++
        j++
        m[num]++
        m[prev_num]--
        
        sum += int64(num - prev_num)

        if m[prev_num] == 0{
            delete(m, prev_num)
        }
        if len(m) >= a && maxSum < sum{
            maxSum = sum
        }
    }
    return maxSum
}
```
## Return a list whose elements are the distinct-character lists for every length-L substring that contains all unique characters.

```python
from typing import List

def unique_chars_in_substring(chars: List[str], L: int) -> List[List[str]]:
    if L<=0 or L>len(chars):
        return []

    seq = ''.join(chars)
    res = []
    # sliding window with two pointers
    left = 0
    seen = {}
    for right, ch in enumerate(seq):
        # ensure uniqueness inside the window
        while ch in seen and seen[ch] >= left:
            left = seen[ch]+1
        seen[ch] = right

        # once the window reaches the desired length
        if right-left+1 == L:
            res.append(seq[left:right+1])
            left+=1

    return res
```
    return res
```
