```text
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome. 
```

```go
package main
func validPalindrome(A string) bool {
    l,r:=0,len(A)-1
    n:=len(A)
    var temp string
    for l<=r{
        if A[l] != A[r]{
            temp = A[:l]
            if l+1<n{
                temp += A[l+1:]
            }
            if temp==reverse(temp){
                return true
            }
            temp = A[:r]
            if r+1<n{         
                temp += A[r+1:]
            }
            if temp==reverse(temp){
                return true
            }else{
                return false
            }
        }else{
            l++
            r--
        }
    }
    return true
}

func reverse(A string) string{
    run := []rune(A)
    l,r := 0,len(A)-1
    for l<r{
        run[l],run[r] = run[r],run[l]
        l++
        r--
    }
    return string(run)
}
```