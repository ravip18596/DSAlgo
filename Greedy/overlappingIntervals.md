Problem
-------
Given a list of time intervals (start, end). Group the overlapping intervals and return an array of arrays.

Example 1 

Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)] 
Output: [[(1, 3), (2, 5)], [(8, 10), (9, 11)], [(15, 21)]]

Example 2
Input: [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]

Output:[(1, 3), (2, 5), (3, 4)], [(8, 10), (9, 11)], [(15, 21)]

Solution
--------

```python
def group_overlapping_intervals(intervals):

  intervals.sort()
  groups = []
  current_group = []
  for interval in intervals:
    if not current_group or interval[0] <= current_group[-1][1]:
      current_group.append(interval)
    else:
      groups.append(current_group)
      current_group = [interval]
  groups.append(current_group)
  return groups


def main():
  intervals = [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
  print(group_overlapping_intervals(intervals))


if __name__ == "__main__":
  main()

```