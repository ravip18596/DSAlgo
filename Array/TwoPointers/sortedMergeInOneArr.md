Problem
--------
https://www.geeksforgeeks.org/sorted-merge-one-array/

Given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
Merge B into A in sorted order.

Examples: 

Input : a[] = {10, 12, 13, 14, 18, NA, NA, NA, NA, NA}   
        b[] = {16, 17, 19, 20, 22};;
Output : a[] = {10, 12, 13, 14, 16, 17, 18, 19, 20, 22}


Solution
--------

- Python

```python
def sortedMerge(a, b, n, m):
    i = n - 1
    j = m - 1
     
    lastIndex = n + m - 1
     
    # Merge a and b, starting from last
    # element in each
    while (j >= 0):
        if (i >= 0 and a[i] > b[j]):
            a[lastIndex] = a[i]
            i -= 1
        else:
            a[lastIndex] = b[j]
            j -= 1
        
        lastIndex-= 1
```