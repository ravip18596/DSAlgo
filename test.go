package main

import "fmt"

func main() {
	a := []int{1, 2}
	a = a[:0]
	fmt.Println(a, len(a), cap(a))

}