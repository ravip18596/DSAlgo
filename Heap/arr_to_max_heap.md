Heap Data Structure Implementation
----------------------------------

- [Heap Notes](https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture4.pdf)

### Time Complexity

- Heapify Operation is `log(n)` or height of heap tree.
- Build Max Heap Operation runtime for n element arr is O(2n) ~ O(n) 

## Implementation

### Max Heap

### Golang
```go
package main

import "fmt"

func maxHeapify(arr []int, i int) {
	leftChild, rightChild := 2*i+1, 2*i+2
	n := len(arr)
	largest := i
	if leftChild < n && arr[leftChild] > arr[largest] {
		largest = leftChild
	}
	if rightChild < n && arr[rightChild] > arr[largest] {
		largest = rightChild
	}

	if largest != i {
		// swap largest index element with parent index element
		arr[largest], arr[i] = arr[i], arr[largest]
		// the other subtree of parent is already a max heap
		// so now check the heap subtree, from where the largest came from, whether that subtree is heap or not
		maxHeapify(arr, largest)
	}
}

func buildMaxHeap(arr []int) {
	// leaf nodes of heap are already trivial max heap.
	// So run heapify operation on parent nodes starting from n/2 to 0
	n := len(arr)
	for i := n/2 - 1; i >= 0; i-- {
		maxHeapify(arr, i)
	}
}

func heapSort(arr []int) {
    // irst we use BuildMaxHeap to turn the array into a max-heap.
    buildMaxHeap(arr)
    n := len(arr)
    // extract the maximum (i.e. the root) from the heap
    // swapping it with the last element in the array 
    for i:=n-1;i>=0;i--{
        arr[0], arr[i] = arr[i], arr[0]
        // At this point, the heap property is violated because the root may be smaller than other elements
        // now the heap property is voilated
        // run heapify on root to restore heap property
        heapify(arr, 0)         
}

func main() {
	arr := []int{3, 2, 1, 5, 6}
	heapSort(arr)
	fmt.Println("sorted arr is ", arr)
}

/* Output
max heap is  [6 5 1 3 2]
*/
```
### Python

```python
from typing import List

arr = [3,2,1,5,6]


# max heapify
def max_heapify(arr: List[int], index: int):
    """
    Time Complexity: log(n) where n is len of arr or equal to height of heap tree
    :param arr:
    :param index:
    :return:
    """
    leftchild, rightchild = 2*index + 1, 2*index + 2
    max_length = len(arr)
    # largest element index is current index
    largest = index
    if leftchild < max_length and arr[largest] < arr[leftchild]:
        largest = leftchild

    if rightchild < max_length and arr[largest] < arr[rightchild]:
        largest = rightchild

    if largest != index:
        # swap largest element with parent
        arr[largest], arr[index] = arr[index], arr[largest]
        # the other subtree of parent is already a max heap
        # so now check the heap subtree, from where the largest came from, whether that subtree is heap or not
        max_heapify(arr, largest)

    return arr


def build_max_heap(arr: List[int]) -> List[int]:
    # leaf nodes of heap are already trivial max heap.
    # So run heapify operation on parent nodes starting from n/2 to 0
    n = len(arr)
    i = n//2
    while i >= 0:
        max_heapify(arr, i)
        i -= 1
    
    return arr

arr = build_max_heap(arr)
print(arr)

# Output
# [6 5 1 3 2]
```
