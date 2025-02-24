# Arrays

## Kadane Algorithm

```python
def kadane_algorithm_with_indices(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = end = s = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return max_sum, start, end

# Example usage:
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# max_sum, start, end = kadane_algorithm_with_indices(arr)
# print(f"Maximum sum is {max_sum} from index {start} to {end}")
# Output: Maximum sum is 7 from index 2 to 6
```

## Trapping Rainwater

>Problem Statement [https://leetcode.com/problems/trapping-rain-water/description/](https://leetcode.com/problems/trapping-rain-water/description/)

> After every position, I will have a possible height of water
$$ actual height of water = min(lmax, rmax) - height of the wall $$

- Python
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # water += min(max_left, max_right) - arr[i]
        # Space: O(N)
        # Time: O(N)
        water = 0
        n = len(height)
        right = [0]*n
        right[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right[i] = max(height[i], right[i+1])

        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])

            water += min(max_left, right[i]) - height[i]

        return water
```
