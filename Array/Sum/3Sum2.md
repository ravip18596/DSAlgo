```text
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

`Solution - Time - O(N2) Space - No extra space`

```go
package main
import "sort"
func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    n := len(nums)
    result := make([][]int,0)
    for i:=0;i<n-2;i++{
        if i>0 && nums[i-1]==nums[i]{
            continue
        }
        //a+b+c=0 => b+c=-a
        a := -1*nums[i]
        b,c:=i+1,n-1
        for b<c{
            sum := nums[b]+nums[c]
            if sum<a{
                b++
            }else if sum>a{
                c--
            }else{
                triplet := []int{nums[i],nums[b],nums[c]}
                b++
                c--
                result = append(result,triplet)
                for b<c && nums[b]==triplet[1]{ b++ }
                for b<c && nums[c]==triplet[2]{ c-- }
            }
        }
    }
    return result
}
```

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list(list())
        if len(nums) < 3:
            return result
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i-1] == nums[i]:
                continue

            sum = -1 * nums[i]
            s,e = i+1,n-1
            while s<e:
                two_sum = nums[s] + nums[e]
                if two_sum < sum:
                    s+=1
                elif two_sum > sum:
                    e-=1
                else:
                    triplet = [ nums[i],nums[s],nums[e] ]
                    result.append(triplet)
                    s,e = s+1,e-1
                    while s<e and nums[s] == triplet[1]:
                        s+=1

                    while s<e and nums[s] == triplet[2]:
                        e-=1

        return result                
```