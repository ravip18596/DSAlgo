Problem
-------
```text
Find max value of |A[i]-A[j]| + |i-j|
```

Examples
--------
```text
Input : A = {3, -2, 5, -4}
Output : 10

Input : A = {1, 3, -1}
Output : 5
```

Solution
--------
```text
Case 1 - [(A[i]+i) - (A[j]+j)]  [max1 - min1]
Case 2 - [(A[i]-i) - (A[j]-j)]  [max2 - min2]
Result = max(max2-min2,max1-min1)
Time - O(N)
Time - O(1)
```
```python
def solve(arr,n):
    max1,max2,min1,min2 = arr[0],arr[0],arr[0],arr[0]
    for i in range(1,n):
        max1 = max(max1,arr[i]+i)
        max2 = max(max2,arr[i]-i)
        min1 = min(min1,arr[i]+i)
        min2 = min(min2,arr[i]-i)
    return max(max2-min2,max1-min1)    
```