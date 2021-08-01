package main

import (
	"fmt"
)

/*
Time Complexity
Tree Construction - O(N) - Total 2n-1 nodes need to be created
Update - O(LogN) - equivalent to the height of segment tree
Range Sum Query - O(LogN) -
*/
type SegmentTree struct {
	tree
}

func main() {
	fmt.Println("Hello, playground")
}
