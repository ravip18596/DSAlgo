```text
 Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
```

```text
The approach is same as Next Greater Element I
See explanation in my solution to the previous problem
The only difference here is that we use stack to keep the indexes of the decreasing subsequence
```

```go
package main
func nextGreaterElements(nums []int) []int {
    //we will store index in array as duplicate will occur due to
    n := len(nums)
    next := make([]int,n)
    if n==0{
        return next
    }
    stack := []int{0}
    for i:=1;i<2*n;i++{
        for len(stack)>0 && nums[i%n] > nums[stack[0]]{
            next[stack[0]] = nums[i%n]
            //pop
            stack = stack[1:]
        }
        if i<n{
            //push
            stack = append([]int{i},stack...)
        }
    }
    for len(stack)>0{
        next[stack[0]] = -1
        stack = stack[1:]
    }
    return next
}
```