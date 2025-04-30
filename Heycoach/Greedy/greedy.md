# Greedy

## Activity Selection Problem

Problem Description: Max Tasks Done

Input:

    The first line contains an integer, N (1 ≤ N ≤ 2*10^5), representing the number of problems.
    The next two lines contain two arrays of size N each:
        The first array contains the starting day of each problem, where 1 ≤ start[i] ≤ 10^9.
        The second array contains the ending day of each problem, where 1 ≤ end[i] ≤ 10^9.

Output:

    Output a single integer representing the maximum number of problems Raman can solve.

### Example

```text
Input:
4
1 2 3 6
3 5 9 8

Output:
2

Explanation:
This input consists of 4 problems with starting days [1, 2, 3, 6] and ending days [3, 5, 9, 8].

To maximize the number of problems Raman can solve, we consider each problem as a tuple of (start, end):

(1, 3), (2, 5), (3, 9), (6, 8).
After sorting by ending days and selecting non-overlapping problems:

Raman can solve Problem 1 (1, 3) and Problem 4 (6, 8).
Thus, the maximum number of problems he can solve is 2.
```

### Solution

```python
class Solution:
    def solve(self, start, end, n):
      #Write your code here
      jobs = []
      for i in range(n):
        jobs.append((start[i], end[i]))

      jobs.sort(key=lambda x:x[1])
      last_finish_time = jobs[0][1]
      cnt = 1
      for i in range(1, n):
        if jobs[i][0] >= last_finish_time:
          cnt += 1
          last_finish_time = jobs[i][1]

      return cnt
```

## Fractional Knapsack

Problem - Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note: Unlike 0/1 knapsack, you are allowed to break the item.

Example 1
```text
Input
N = 3, W = 50
values = [60,100,120]
weight = [10,20,30]
Output
240.00
Explanation:
Initial W = 50. take item 1 with weight 10 and value 60 so W is now 50 - 10 = 40.
take item 2 with weight 20 and value 100 so W is now 40 - 20 = 20.
Now, we cannot take item 3 completely so we will just take W = 20 amount of it
and the value we will get out of it is 80 and W becomes 20 - 20 = 0.
so total value is 60 + 100 + 80 = 240.
So,Total maximum value of item we can have is 240.00 from the given capacity of sack.
```

Solution
```python
def fractional_knapsack(values, weights, W):
    # Calculate value to weight ratio for each item
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
    
    # Sort items by value to weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0  # Total value accumulated in the knapsack
    
    for value, weight, ratio in items:
        if W == 0:  # If the knapsack is full, break out of the loop
            break
        if weight <= W:  # If the item can be added completely
            total_value += value
            W -= weight
        else:  # If the item cannot be added completely
            total_value += ratio * W  # Add the fraction of the item that fits
            W = 0  # The knapsack is now full
    
    return total_value

# Example usage
N = 3
W = 50
values = [60, 100, 120]
weights = [10, 20, 30]

max_value = fractional_knapsack(values, weights, W)
print(f"{max_value:.2f}")  # Output: 240.00
```
