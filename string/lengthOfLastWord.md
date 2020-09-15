Problem
------
```text
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the last appearing word 
if we loop from left to right) in the string.

If the last word does not exist, return 0.
```

Examples
--------
```text
Input: "Hello World"
Output: 5

Input: "   Hello W$orld    "
Output: 6
```
Solution
--------
```text
time  - bigO(N) // where n is the len of the input string
space - bigO(1) // No extra space
```
```go
package main
func lengthOfLastWord(s string) int {
    var cnt int
    n := len(s)
    if n==0{
        return cnt
    }
    var foundChar bool
    foundChar = false
    for i:=n-1;i>=0;i--{
        if s[i]==' '{
            if foundChar{
                break
            }
        }else{
            cnt+=1
            foundChar = true
        }
    }
    return cnt
}
```