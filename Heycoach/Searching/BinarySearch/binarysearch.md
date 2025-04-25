# Binary Search

## Maximum Candies Allocated to K Children

[2226. Maximum Candies Allocated to K Children](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/)

```python
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        def check(mid: int) -> bool:
            cnt = 0
            for i in range(n):
                cnt += candies[i]//mid
            if cnt >= k:
                return True
            return False
        
        low, high = 1, max(candies)
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if check(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1

        return ans
```

## House Robber

[2560. House Robber IV](https://leetcode.com/problems/house-robber-iv/description/)

```python

```
