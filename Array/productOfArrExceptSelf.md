Solution
--------

- Time Complexity - O(N)
- Space Complexity - O(1)

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n
        #calculated the left side sum
        #nums = [1,2,3,4]
        #nums[i-1]=1, result[i-1]=1,[1, 1, 1, 1]
        #nums[i-1]=2, result[i-1]=1,[1, 1, 2, 1]
        #nums[i-1]=3, result[i-1]=2,[1, 1, 2, 6]
        for i in range(1,n):
            result[i] = nums[i-1] * result[i-1]
            # print(f"nums[i-1]={nums[i-1]}, result[i-1]={result[i-1]},result={result}")
            
            
        right = 1
        # right is 1, result - [1,1,2,6]
        # right is 4, result - [1, 1, 2, 6]
        # right is 12, result - [1, 1, 8, 6]
        # right is 24, result - [1, 12, 8, 6]
        # right is 24, result - [24, 12, 8, 6]
        for i in range(n-1,-1,-1):
            result[i] *= right
            right *= nums[i]
            # print(f"right is {right}, result - {result}")
            
        
        return result
```