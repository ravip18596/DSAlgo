Problem
-------
Given a string s and a character c that occurs in s, return an array of integers answer where `answer.length == s.length` and `answer[i]` is the shortest distance from s[i] to the character `c` in `s`.

Example 1:
```text
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
```
Example 2:
```text
Input: s = "aaab", c = "b"
Output: [3,2,1,0]
```

Solution
--------
- Time O(N) ~N is len of string 
- Space O(N)

### Intution
For each index S[i], let's try to find the distance to the next character C going left, and going right.
The answer is the minimum of these two values.

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans  = [0]*n
        prev = -1
        for i,ch in enumerate(s):
            prev = i if ch==c else prev
            ans[i] = i-prev if prev != -1 else n+1
            
        nex = -1
        for i in range(n-1,-1,-1):
            nex = i if s[i]==c else nex
            ans[i] = min(ans[i],nex-i) if nex != -1 else ans[i]
        
        return ans
```

```go
package main
func shortestToChar(s string, c byte) []int {
    chars := []rune(s)
    prev := -1
    result := make([]int,len(chars))
    for i:=0;i<len(result);i++{
        //initialize with max value
        result[i] = len(result)+1
    }
    for i,ch := range chars{
        if byte(ch)==c{
            prev = i
        }
        if prev != -1{
            result[i] = i-prev
        }
    }
    prev = -1
    for i:=len(chars)-1;i>=0;i--{
        if byte(chars[i])==c{
            prev = i
        }
        if prev != -1{
            result[i] = min(result[i],prev-i)
        }
    }
    return result
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}
```