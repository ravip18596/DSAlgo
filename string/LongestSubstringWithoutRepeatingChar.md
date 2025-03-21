  Problem
-------
Given a string s, find the length of the longest substring without repeating characters.

Example
-------
```text
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""   
Output: 0
```


Solution
--------
the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values,
and keep two pointers which define the max substring.
move the right pointer to scan through the string, and meanwhile update the hashmap. If the character is already in the hashmap, then move the left pointer to the right of the same character last found. Note that the two pointers can only move forward.
Using hashmap to store last occurrence of char and start maintains the current distinct sub-array window
- Time - O(N)
- Space - O(255) ~ O(1) 

`Golang`
```go
package main
func lengthOfLongestSubstring(s string) int {
    if len(s)==0{
        return 0
    }
    m := make(map[int32]int)
    var maxLen int
    var start int
    start = -1
    for i,c:=range s{
        if _,ok:=m[c];ok{
            if m[c] > start{
                start = m[c]
            }
        }
        m[c] = i
        if maxLen < i-start{
            maxLen = i-start
        }
    }
    return maxLen
}
```
`Python`
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        ch_map = [-1]*256
        left = -1
        max_len = 0
        for i, c in enumerate(s):
            if ch_map[ord(c)] != -1:
                if ch_map[ord(c)] > left:
                    "update left only if index is to the right of previous left"
                    left = ch_map[ord(c)]
            
            ch_map[ord(c)] = i
            max_len = max(max_len, i-left)
        
        
        return max_len
```
