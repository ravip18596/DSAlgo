`Problem`
```text
Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

If it is possible then return 1 else return 0.
```
`Solution`

```go
package main
func solve(A string )  (int) {
    l,r:=0,len(A)-1
    var once bool
    for l<=r{
        if A[l] != A[r]{
            if once {
                return 0
            }
            once = true
            if A[l+1]==A[r]{
                l++
            }else if A[l] == A[r-1]{
                r--
            }else{
                return 0
            }
            
        }else{
            l++
            r--
        }
    }
    return 1
}
```

or

```go
package main
func solve(A string )  (int) {
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
                return 1
            }
            temp = A[:r]
            if r+1<n{         
                temp += A[r+1:]
            }
            if temp==reverse(temp){
                return 1
            }else{
                return 0
            }
        }else{
            l++
            r--
        }
    }
    return 1
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