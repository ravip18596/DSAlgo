```text
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

`Solution`

`Python`
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n<=0:
            return -1
        
        rotated = 0
        if nums[0] > nums[n-1]:
            for i in range(n-1):
                rotated += 1
                if nums[i] > nums[i+1]:
                    break
        
        return self.binary_search(nums,rotated,target)
    
    def binary_search(self, nums: List[int], rotated: int, target: int) -> int:
        n = len(nums)
        s,e = 0,n-1
        while s<=e:
            m = (s+e)//2
            rotated_m = (m+rotated)%n
            if nums[rotated_m] == target:
                return rotated_m
            elif nums[rotated_m] > target:
                e = m-1
            else:
                s = m+1
            
        return -1
```

`Golang`

```go
package main

func search(nums []int, target int) int {
    rotation := 0
    n := len(nums)
    if n==0{
        return -1
    }
    if nums[0] > nums[n-1]{
        for i:=0;i<n-1;i++{
            rotation+=1
            if nums[i] > nums[i+1]{
                break
            }
        }
    }
    fmt.Println(rotation)
    return binarySearch(nums,target,rotation)
}

func binarySearch(nums []int,target int,rotated int) int{
    s := 0
    e := len(nums)-1
    n := len(nums)
    
    for s<=e{
        m := int((s+e)/2)
        if nums[(m+rotated)%n] > target{
            e = m-1
        }else if nums[(m+rotated)%n] < target{
            s = m+1
        }else{
            return (m+rotated)%n
        }
    }
    return -1
}
```