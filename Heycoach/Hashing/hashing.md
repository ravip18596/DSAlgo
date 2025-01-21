# Hashing

## Subarray with k-sum

Given an array of integers nums. Find all the subarrays with sum k

$$Time Complexity: O(n)$$

```python
def subarray_with_k_sum(nums: List[int], k: int) -> List[List[int]]:
    n = len(nums)
    prefix_sum = {0: -1}  # Initialize prefix sum hashmap with 0 sum at index -1
    current_sum = 0
    res = []

    for i in range(n):
        current_sum += nums[i]
        if current_sum - k in prefix_sum:
            start_index = prefix_sum[current_sum-k] + 1
            res.append([start_index, i])
        prefix_sum[current_sum] = i

    return res


def subarray_with_k_sum(nums: List[int], k: int) -> List[List[int]]:
    n = len(nums)
    prefix_sum = {0: -1}  # Initialize prefix sum hashmap with 0 sum at index -1
    current_sum = 0
    for i in range(n):
        current_sum += nums[i]
        prefix_sum[current_sum] = i

    res = []
    for i in range(n):
        if current_sum - k in prefix_sum:
            start_index = prefix_sum[current_sum-k] + 1
            res.append([start_index, i])

    return res
```

## Find the total count of subarray that sums to k

$$ Time Complexity: O(n) $$

```python
def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum = {0: 1}
    current_sum = 0
    n = len(nums)
    cnt = 0
    
    for i in range(n):
        current_sum += nums[i]
        if current_sum - k in prefix_sum:
            cnt += prefix_sum[current_sum-k]

        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return cnt
```

## Find the len of the longest possible subarray that sums to k

if there are multiple such subarrays with lowest starting index

$$ Time Complexity: O(n) $$

```python
def longest_subarray_with_k_sum(nums: List[int], k: int) -> int:
    """
    Returns the length of the longest possible subarray that sums to k.
    If there are multiple such subarrays with the same length, returns the one with the lowest starting index.

    Args:
        nums (List[int]): The input list of integers.
        k (int): The target sum.

    Returns:
        int: The length of the longest possible subarray that sums to k.
    """
    n = len(nums)
    prefix_sum = {0: -1}  # Initialize prefix sum hashmap with 0 sum at index -1
    current_sum = 0
    max_len = 0
    min_start_idx = float('inf')

    for i in range(n):
        current_sum += nums[i]
        if current_sum - k in prefix_sum:
            if i - prefix_sum[current_sum - k] > max_len:
                max_len = i - prefix_sum[current_sum - k]
                min_start_idx = prefix_sum[current_sum - k] + 1
            elif i - prefix_sum[current_sum - k] == max_len:
                min_start_idx = min(min_start_idx, prefix_sum[current_sum - k] + 1)
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return max_len
```

## Two Sum

Solution using hashmaps

$$ Time-Complexity: O(n) $$
$$ Space-Complexity: O(n) $$

```python
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns the indices of the two numbers in the input list that add up to the target sum.

    Args:
        nums (List[int]): The input list of integers.
        target (int): The target sum.

    Returns:
        List[int]: The indices of the two numbers that add up to the target sum.
    """
    num_map = {}  # Initialize hash map to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement of the current number
        if complement in num_map:  # Check if the complement is in the hash map
            return [num_map[complement], i]  # Return the indices of the two numbers
        num_map[num] = i  # Store the current number and its index in the hash map

    return []  # Return an empty list if no solution is found
```

