Problem
-------
```text
You are given a string s of even length. Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
```
`Example`
```text
Input: s = "AbCdEfGh"
Output: true
```
Solution
--------
```text
Time -  O(N) N - is the length of the string
Space - O(1) 
```

`Python`
```python
class Solution:    
    def count_vowels(self,s: str) -> int:
        count = 0
        for c in s:
            if c in "aeiou":
                count+=1
        
        return count

        
    def halvesAreAlike(self, s: str) -> bool:
        #print(s[:len(s)//2].lower(), self.count_vowels(s[:len(s)//2].lower()))
        #print(s[len(s)//2:].lower(), self.count_vowels(s[len(s)//2:].lower()))
        return self.count_vowels(s[:len(s)//2].lower()) == self.count_vowels(s[len(s)//2:].lower())
        
```

`Golang`
```go
import "strings"

func countVowels(s []rune) int{
    cnt := 0
    for i:=0;i<len(s);i++{
        if s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u'{
            cnt++
        }
    }
    return cnt
}

func halvesAreAlike(s string) bool {
    strRune := []rune(strings.ToLower(s))
    n := len(strRune)
    return countVowels(strRune[:n/2]) == countVowels(strRune[n/2:])
}
```