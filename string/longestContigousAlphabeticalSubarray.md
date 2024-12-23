Problem
-------

2414. Length of the Longest Alphabetical Continuous Substring



An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

    For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.

Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

Example 1:

Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.

Example 2:

Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.

 

Constraints:

    1 <= s.length <= 105
    s consists of only English lowercase letters.


Solution
--------

```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        start, max_length =0, 0
        n = len(s)
        for i in range(1,n):
            diff = ord(s[i]) - ord(s[i-1])
            if diff != 1:
                start=i
                
                
            max_length = max(max_length, i-start+1)
            
        return max_length
```
