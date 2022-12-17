Problem Statement
-----------------
Given a string, find substring of length k such that it
contains maximum number of vowels. 
- In case, 2 substrings contains equal number of vowels then pick the one with
least starting index. 
- If there is no substring with vowels then return "Not Found!"

Examples
---------
 
- str = "azexbiq"
- k = 4

Solution:
azex

Solution
--------
- Maintain a prefix vowel count

```python
def vowel_substr(s, k):
    n = len(s)
    #   a z e x b i q
    # 0 1 1 2 2 2 3 3
    vowel_count_prefix = [0]*(n+1)
    for i,c in enumerate(s):
        is_vowel = 1 if c in 'aeiou' else 0
        vowel_count_prefix[i+1] = vowel_count_prefix[i] + is_vowel
    
    max_cnt, max_str = 0, ''
    for i in range(n-k):
        a,b = i, i+k
        vowel_cnt = vowel_count_prefix[b+1] - vowel_count_prefix[a]
        if vowel_cnt > max_cnt:
            max_cnt = vowel_cnt
            max_str = s[a:b]
    
    if max_cnt == 0:
        max_str = "Not Found!"
    return max_str
```
