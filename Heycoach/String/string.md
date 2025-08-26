# String

## Is Subsequence

```python
def isSubsequence(s: str, t: str) -> bool:
    i, j, m, n = 0, 0, len(s), len(t)
    while i<m and j<n:
        if s[i]==t[j]:
            i+=1

        j+=1
    
    return i==m
```

## Create largest concatenated number

Question - [https://www.geeksforgeeks.org/dsa/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/](https://www.geeksforgeeks.org/dsa/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/)

```python
from functools import cmp_to_key

def compare(x,y):
    if x+y > y+x:
        return -1
    else:
        return 1
        
def findLargest(arr):
    nums = [str(i) for i in arr]
    nums.sort(key=cmp_to_key(compare))
    if nums[0] == '0':
        # sorting in decreasing order
        # if first num is zero, then rest is zero
        return '0'
    return ''.join(nums)

arr = [3, 30, 34, 5, 9]
print(findLargest(arr))
```
