Problem
-------
```text
Suppose you have a sorted array of infinite numbers, 
how would you search an element in the array?
```

Solution
--------
```text
If the array is infinite, that means we don’t have proper bounds to apply binary search. 
So in order to find position of key, first we find bounds and then apply binary search algorithm.
```
```go
package main
func binarySearch(arr []int,target int,start,end int) int{
	for start<end{
		mid := start + (end-start)>>1
		if arr[mid]==target{
			return mid
		}
		if arr[mid]<target{
			start=mid+1
		}else{
			end=mid-1
		}
	}
	return -1
} 

// function takes an infinite size array and a key to be 
//  searched and returns its position if found else -1. 
// We don't know size of arr[] and we can assume size to be 
// infinite in this function. 
func findIndex(arr []int,target int) int{
	l,h:=0,1
	if arr[0]==target{
		return 0
	}
	val := arr[h]
	for val < target{
		l = h
		h *= 2
		val = arr[h]
	}
	return binarySearch(arr,target,l,h)
}
```