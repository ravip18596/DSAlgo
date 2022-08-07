Solution
--------

```python
def shipWithinDays(self, weights: List[int], days: int) -> int:
    # 1. capacity should be at least max(weights), otherwise the conveyor belt couldn't ship the heaviest package. 
    # 2. capacity need not be more than sum(weights), because then we can ship all packages in just one day.
    
    # 3. we will range over from min ship weight capacity to max ship weight capacity to identify the weight capacity that allows packages to be shipped within days.
    
    def feasible(capacity: int) -> bool:
        day, day_sum = 0, 0
        for weight in weights:
            day_sum += weight
            if day_sum > capacity:
                day += 1
                day_sum = weight # this weight will go on the next day ship
                if day > days:
                    return False # crosses d days timeline, so this capacity is not feasible
        
        return True # feasible with this capacity
    
    left, right = min(weights), max(weights)
    while left < right:
        mid_capacity = left + (right-left)//2
        if feasible(mid_capacity):
            # now reduce search space from right to find min ship weight that is feasible
            right = mid_capacity
        else:
            # reduce search space in the left
            left = mid_capacity + 1
            
    return left
```
