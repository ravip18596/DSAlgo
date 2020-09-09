Problem
-------
```text
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.


Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

```
Solution
--------
```text
Time - O(N)
Space - O(N)
```
```go
package main
//nC2 - because you have n indexes to play 2 places (becoz - pairs) 
func numIdenticalPairs(nums []int) int {
    m := make(map[int]int)
    for _,num := range nums{
        m[num]+=1
    }
    var pairs int
    for _,val:=range m{
        pairs += (val*(val-1))/2
    }
    return pairs
}
```