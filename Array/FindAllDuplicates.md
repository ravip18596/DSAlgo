Problem
-------

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example
-------
```text
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

Solution
--------
`Python`
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
          0  1  2  3  4  5  6  7 
        [ 4, 3, 2, 7, 8, 2, 3, 1] inital
        [ 4, 3, 2,-7, 8, 2, 3, 1] i=0 arr[4-1] = arr[3]
        [ 4, 3,-2,-7, 8, 2, 3, 1] i=1 arr[3-1] = arr[2]
        [ 4,-3,-2,-7, 8, 2, 3, 1] i=2 arr[2-1] = arr[1]
        [ 4,-3,-2,-7, 8, 2,-3, 1] i=3 arr[7-1] = arr[6]
        [ 4,-3,-2,-7, 8, 2,-3,-1] i=4 arr[8-1] = arr[7]
        [ 4,-3,-2,-7, 8, 2,-3,-1] i=5 arr[2-1] = arr[1]
        [ 4,-3,-2,-7, 8, 2,-3,-1] i=6 arr[3-1] = arr[2]
        [-4,-3,-2,-7, 8, 2,-3,-1] i=7 arr[1-1] = arr[0]
        when find a number i, flip the number at position i-1 to negative.
        if the number at position i-1 is already negative, i is the number that occurs twice.
        '''
        
        twice_occ_ele = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] *= -1
            else:
                twice_occ_ele.append(abs(nums[i]))
                
        return twice_occ_ele
```
`Go`
```go
package main
//when find a number i, flip the number at position i-1 to negative. 
//if the number at position i-1 is already negative, i is the number that occurs twice.
func findDuplicates(nums []int) []int {
    var duplicates []int
    var index int
    for i:=0;i<len(nums);i++{
        index = abs(nums[i])-1
        if nums[index]>0{
            nums[index] *= -1
        }else{
            duplicates = append(duplicates,abs(nums[i]))
        }
    }
    return duplicates
}

func abs(a int)int{
    if a<0{
        return -1*a
    }
    return a
}
```