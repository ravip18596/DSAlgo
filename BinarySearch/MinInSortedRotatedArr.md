```text
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
```

`Solution - O(n)`
```go
package main
func findMin(nums []int) int {
    //check if it rotated
    if len(nums)==1{
        return nums[0]
    }
    n := len(nums)
    if nums[0]<nums[n-1]{
        return nums[0]
    }
    for i:=1;i<n;i++{
        if nums[i-1]>nums[i]{
            return nums[i]
        }
    }   
    return 0
}
```

`Solution - O(logN)`

```go
package main
func findMin(nums []int) int {
    //check if it rotated
    low,high := 0,len(nums)-1
    for low<high{
        mid := low + (high-low)>>1
        if nums[mid]>nums[high]{
            // it means that min is on the right
        	low = mid+1
        }else{
            high=mid
        }
    }
    return nums[low]
}

```

`Above problem with duplicates allowed`

```go
package main
func findMin(nums []int) int {
    //check if it rotated
    low,high := 0,len(nums)-1
    for low<high{
        mid := low + (high-low)>>1
        if nums[mid]>nums[high]{
            // it means that min is on the right
        	low = mid+1
        }else if nums[mid]<nums[high]{
            high=mid
        }else{
        	//arr[mid]==arr[high]
        	high--
        }
    }
    return nums[low]
}
```
