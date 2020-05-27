#String Problems

### Question 1
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


### Solution 1

```go
// this solution supports unicode characters 
package main
import "fmt"
func isAnagram(s string, t string) bool {
    //boundary conditions
    if len(s)!=len(t){
        return false
    }
    m := make(map[rune]int)
    for _,c:= range s{
        if _,ok:=m[c];!ok{
            m[c]=1
        }else{
            m[c]+=1
        }
    }
    
    for _,c:=range t{
        if m[c]<=0{
            return false
        }
        m[c]-=1
    }
    return true
}

func main(){
	fmt.Println(isAnagram("ram","car"))
}
```

