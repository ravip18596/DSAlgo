```text
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

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