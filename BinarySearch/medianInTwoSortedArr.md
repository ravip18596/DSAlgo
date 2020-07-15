`Problem`

```text
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

`Solution`

```go
package main
const(
    INT_MIN = -1 * int(1e10)
    INT_MAX = int(1e10)
)
//partitionY + partitionX = (x+y+1)/2
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    x := len(nums1)
    y := len(nums2)
    if x>y{
        return findMedianSortedArrays(nums2,nums1)
    }
    start,end := 0,x
    for start <= end{
        partitionX := (start+end)>>1
        partitionY := (x+y+1)>>1 - partitionX
        minRightX,minRightY,maxLeftX,maxLeftY := INT_MAX,INT_MAX,INT_MIN,INT_MIN
        if partitionX>0{ maxLeftX = nums1[partitionX-1] }
        if partitionY>0{ maxLeftY = nums2[partitionY-1] }
        if partitionX<x{ minRightX = nums1[partitionX] }
        if partitionY<y{ minRightY = nums2[partitionY] }
        //fmt.Println(partitionX,partitionY,maxLeftX,maxLeftY,minRightX,minRightY)
        if maxLeftX <= minRightY && maxLeftY <= minRightX{
            if (x+y)&1 ==1{
                //odd
                return float64(max(maxLeftX,maxLeftY))
            }else{
                //even
                return (float64(max(maxLeftX,maxLeftY)) + float64(min(minRightX,minRightY)))/2
            }
        }else if maxLeftX > minRightY{
            end = partitionX-1
        }else{
            start = partitionX+1
        }
    }
    return 0.0
}

func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}
```