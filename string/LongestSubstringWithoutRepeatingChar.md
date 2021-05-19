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

Using hashmap to store last occurrence of char and start maintains the current distinct sub-array window
- Time - O(N)
- Space - O(N)

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

```