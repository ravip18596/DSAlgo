```text
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
```

```go
package main
import "strings"

func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    //fmt.Println(s)
    for i,j:=0,len(s)-1;i<=j;{
        if !((s[i]>='a' && s[i]<='z') || (s[i]>='0' && s[i]<='9')){
            i++
        }else if !((s[j]>='a' && s[j]<='z')|| (s[j]>='0' && s[j]<='9')){
            j--
        }else if s[i]!=s[j]{
            return false
        }else{
            i++;j--
        }
        
    }
    return true
}
```