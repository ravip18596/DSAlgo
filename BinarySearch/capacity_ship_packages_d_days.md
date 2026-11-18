Solution
--------

```python
"""
A conveyor belt has packages that must be shipped from one port to another within `days` days.

The i-th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship
with packages on the conveyor belt (in the order given by `weights`). We may not load more
weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the
conveyor belt being shipped within `days` days.

Constraints:
- 1 <= days <= len(weights) <= 5 * 10^4
- 1 <= weights[i] <= 500
"""
from typing import List

def feasible(cap, weights, days) -> bool:
    n = len(weights)
    current_load = weights[0]
    days_used = 1

    for i in range(1, n):
        if current_load+weights[i] > cap:
            current_load = 0
            days_used += 1

        current_load += weights[i]

    return days_used<=days

def shipWithinDays(weights: List[int], days: int) -> int:
    min_cap, max_cap = max(weights), sum(weights)
    res = 0
    while min_cap <= max_cap:
        mid = (min_cap+max_cap)//2
        if feasible(mid, weights, days):
            res = mid
            max_cap = mid-1
        else:
            min_cap = mid+1

    return res


if __name__ == '__main__':
    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    output = shipWithinDays(weights, days)
    print(output)
```
