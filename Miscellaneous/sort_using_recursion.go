package main

import "fmt"

func recursiveBubbleSort(arr []int, n int) {
	if n == 1 {
		return
	}
	for i := 0; i < n-1; i++ {
		if arr[i] > arr[i+1] {
			arr[i], arr[i+1] = arr[i+1], arr[i]
		}
	}
	recursiveBubbleSort(arr, n-1)
}

func main() {
	arr1 := []int{5, 1, 4, 2, 8}
	fmt.Println("Unsorted array (Bubble Sort):", arr1)
	recursiveBubbleSort(arr1, len(arr1))
	fmt.Println("Sorted array (Bubble Sort):", arr1)
}
