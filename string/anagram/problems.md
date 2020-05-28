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

`go solution`
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
`python solution`

```python
def isAnagram(s,t)->bool:
    if len(s)!=len(t):
        return False
    m = dict()
    for c in s:
        if c in m:
            m[c]+=1
        else:
            m[c]=1
    
    for c in t:
        if c not in m:
            return False
        if m[c]<=0:
            return False
        m[c]-=1
        
    return True
```

###Problem 2

Given a collection of distinct integers, return all possible permutations.

Example:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```
`python`

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        self.util(nums,[],result)
        return result
    
    def util(self,nums: List[int],path: List[int],result :List[List[int]]):
        if not nums:
            result.append(path)
        """   
         print(nums,path)
         [1, 2, 3] []
         [2, 3] [1]
         [3] [1, 2]
         [] [1, 2, 3]
         [2] [1, 3]
         [] [1, 3, 2]
         [1, 3] [2]
         [3] [2, 1]
         [] [2, 1, 3]
         [1] [2, 3]
         [] [2, 3, 1]
         [1, 2] [3]
         [2] [3, 1]
         [] [3, 1, 2]
         [1] [3, 2]
         [] [3, 2, 1]
        """
        for i in range(len(nums)):
            self.util(nums[:i]+nums[i+1:],path+[nums[i]],result)

```

`cpp`

```
void permute(string str,int l,int r,vector<string>& v){
    if(l==r)
            v.push_back(str);
    else{
        for(int i=l;i<=r;i++){
            swap(str[l],str[i]);
            permute(str,l+1,r,v);
            swap(str[l],str[i]);
        }
    }
}
```

