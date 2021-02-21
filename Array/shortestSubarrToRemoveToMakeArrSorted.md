Problem
-------

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
A subarray is a contiguous subsequence of the array.
Return the length of the shortest subarray to remove.

Examples
--------
```text
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
```
Solution
--------

Thought Process
- Scan from left to right, find the first index left that A[left] > A[left + 1].
- If left == N - 1, this array is already non-descending, return 0.
- Scan from right to left, find the first index right that A[right - 1] > A[right]
- Now we loosely have two options, either deleting the left-side right nodes, or deleting the right-side N - left - 1 nodes.
- So the answer is at most min(N - left - 1, right).
- Now we can use a sliding window / two pointers to get tighter result.
- Let i = 0, j = right. And we examine if we can delete elements between i and j by comparing A[i] and A[j].
- Case 1: A[j] >= A[i], we can delete elements inbetween, so we can try to update the answer using j - i - 1 and increment i to tighten the window.
- Case 2: A[j] < A[i], we can't delete elements inbetween, so we increment j to loosen the window.

```text
Time  - O(N) 
Space - O(1)
```
```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n<=1: # there will be no need to sort less than 2 len list
            return 0
        
        # find left index till when arr is sorted
        left,right = 0,n-1
        while left<n-1 and arr[left] <= arr[left+1]:
            left+=1
        
        if left == n-1: # the arr is sorted
            return 0
            
        # find rightmost index till which arr is sorted    
        while right>0 and arr[right-1] <= arr[right]:
            right-=1
        
        length = min(n-left-1,right)
        #print(left,right,length)
        
        # using sliding window to further reduce this length
        start,end = 0,right
        
        while start <= left and end < n:
            if arr[start] > arr[end]:
                end+=1
            else:
                length = min(length, end-start-1)
                #print(start,end,length)
                start+=1
        return length
        
```

```go
package main
func findLengthOfShortestSubarray(arr []int) int {
    n := len(arr)
    if n<=1{
        return 0
    }
    left,right:=0,n-1
    for left<n-1 && arr[left] <= arr[left+1]{
        left++   
    }
    if left==n-1{
        //it means the arr is already sorted asc
        return 0
    }
    for right>0 && arr[right-1] <= arr[right]{
        right--
    }
    //sliding window - [start,end]
    start,end := 0,right
    //initialise window length
    length := min(n-1-left,right) 
    for start<=left && end<n{
        if arr[start] > arr[end]{
            end++
        }else{
            length = min(length,end-start-1)
            start++
        }
    }
    return length
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}
```