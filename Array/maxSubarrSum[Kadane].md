## Problem

Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

## Example
Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.

Example 2:

Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)

- Python

```python
    def maxSubArraySum(self,arr,N):
        ##Your code here
        n = len(arr)
        current_sum, max_so_far = 0, -1*int(1e7) -1
        for i in range(n):
            current_sum += arr[i]
            if current_sum < 0:
                current_sum = 0
            else:
                max_so_far = max(max_so_far, current_sum)
            
        if max_so_far == -1*int(1e7)-1:
            max_so_far = max(arr)
    
        return max_so_far
```