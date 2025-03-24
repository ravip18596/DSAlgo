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
