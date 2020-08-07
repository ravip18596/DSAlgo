```text
Given an array of distinct elements, find previous greater element for every element. If previous greater element does not exist, print -1.

Examples:

Input : arr[] = {10, 4, 2, 20, 40, 12, 30}
Output :         -1, 10, 4, -1, -1, 40, 40

Input : arr[] = {10, 20, 30, 40}
Output :        -1, -1, -1, -1

Input : arr[] = {40, 30, 20, 10}
Output :        -1, 40, 30, 20
```


```go
package main
func previousGreaterElement(arr []int) []int{
	n := len(arr)
	if n==0{
		return []int{}
	}
	prevGreater := make([]int,n)
	prevGreater[0]=-1 //there is no ele to the left
	stack := []int{arr[0]} //with the first element
	for i:=1;i<n;i++{
		//stack will store element in decreasing sub-sequence order
		for len(stack)>0 && arr[i] > stack[0]{
			//pop
			stack = stack[1:]
		}
		if len(stack)==0{
			//no ele to left is greater than nums[i]
			prevGreater[i] = -1
		}else{
			//the top of the stack stores the element which 
			//is the first greatest element from left side
			prevGreater[i] = stack[0]
		}
		//push
		stack = append([]int{arr[i]},stack...)
	}
	return prevGreater
}
```