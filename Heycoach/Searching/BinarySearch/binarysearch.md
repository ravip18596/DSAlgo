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
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def canSteal(mid: int) -> bool:
            cnt = 0
            i = 0
            while i<n:
                # if current house has less than max robber can steal (mid)
                if nums[i] <= mid:
                    cnt+=1
                    # extra increment to prevent robbing adjacent house
                    i+=1 
                i+=1
            
            return cnt >= k
        
        low, high = 1, max(nums)
        ans = high
        while low <= high:
            mid = (low+high)//2
            if canSteal(mid):
                ans = mid
                high = mid-1
            else:
                low = mid + 1

        return ans
```
