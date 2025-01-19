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
