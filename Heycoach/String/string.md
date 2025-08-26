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

```
