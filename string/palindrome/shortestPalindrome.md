```text
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"

```

`Solution`

`Time Complexity - O(n2) Space - O(n)`

```go
package main
//longest palindromic prefix
func shortestPalindrome(str string) string {
    for i:=len(str);i>0;i--{
        if isPalindrome(str[:i]){
            return reverse(str[i:]) + str
        }
    }
    return ""
}

func isPalindrome(str string) bool{
    l,r:=0,len(str)-1
    for ;l<=r;l,r=l+1,r-1{
        if str[l] != str[r]{
            return false
        }
    }
    return true
}

func reverse(str string) string{
    run := []rune(str)
    for l,r:=0,len(run)-1;l<r;l,r=l+1,r-1{
        run[l],run[r] = run[r],run[l]
    }
    return string(run)
}
```