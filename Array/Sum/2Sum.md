## Problem
Given arr, find index of 2 integer that sum to target
Example 1:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 2:

Input: nums = [3,3], target = 6
Output: [0,1]

## Solution
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    m = {}

    for i,ele in enumerate(nums):
        key = target - ele
        if key in m.keys() and m[key] != i:
            if m[key] < i:
                return [m[key], i]
            else:
                return [i, m[key]]
        m[nums[i]] = i
```

