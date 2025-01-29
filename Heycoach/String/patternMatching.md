# String Pattern Matching

## KMP (Knuth-Morris-Prath) Algorithm

LPS - Longest Prefix Suffix

> LPS of a given string is the longest proper prefix of the string that is also a proper suffix

### LPS of a string

```python
def calc_lps(s: str) -> List[int]:
    # i=1 because lps[0] is 0
    i, n = 1, len(s)
    Len = 0
    lps = [0] * n
    while i<n:
        if s[i] == s[Len]:
            lps[i] = Len+1
            Len += 1
            i += 1
        else:
            if Len == 0:
                lps[i] = 0
                i += 1
            else:
                Len = lps[Len-1]
    
    return lps

if __name__ == '__main__':
    s = "aacaaaac"
    print(calc_lps(s))
    # prints [0, 1, 0, 1, 2, 2, 2, 3]
```


## Longest Happy Prefix

[https://leetcode.com/problems/longest-happy-prefix/description/](https://leetcode.com/problems/longest-happy-prefix/description/)

```python
def longestPrefix(self, s: str) -> str:
    i = 1
    n = len(s)
    Len = 0
    lps = [0] * n
    while i<n:
        if s[i] == s[Len]:
            lps[i] = Len+1
            Len += 1
            i += 1
        else:
            if Len == 0:
                lps[i] = 0
                i += 1
            else:
                Len = lps[Len-1]
    
    return s[:Len]
```
