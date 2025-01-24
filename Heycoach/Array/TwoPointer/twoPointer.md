# Two Pointers

## 2 Sum

 - Time complexity  - O(nlogn) + O(n) = O(nlogn)

```python
def two_sum(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]
```

## 3 Sum

- Time Complexity  - O(nlogn) + O(n^2) = O(n^2)

```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

# Example usage:
# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Container With Most Water

>Problem Statement - [https://leetcode.com/problems/container-with-most-water/description/](https://leetcode.com/problems/container-with-most-water/description/)

- Python
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        l,r = 0, n-1

        while l<r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
```


