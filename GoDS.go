package main

import (
	"fmt"
)

func create2DMatrix(row, col int) [][]interface{} {
	arr := make([][]interface{}, row)
	for i := 0; i < len(arr); i++ {
		arr[i] = make([]interface{}, col)
	}
	return arr
}

type Stack struct {
	cap int
	arr []interface{}
}

func InitStack(size int) *Stack {
	return &Stack{
		cap: size,
		arr: make([]interface{}, 0, size),
	}
}

func (s *Stack) Push(x interface{}) {
	if len(s.arr) == s.cap {
		return
	}
	s.arr = append(s.arr, x)
}

func (s *Stack) Pop() interface{} {
	if len(s.arr) == 0 {
		return nil
	}
	temp := s.arr[len(s.arr)-1]
	s.arr = s.arr[:len(s.arr)-1]
	return temp
}

/*
Heap
*/

func main() {
	// 2-D array
	_ = create2DMatrix(10, 10)
	// stack
	s := InitStack(2)
	s.Push(1)
	s.Push(2)
	fmt.Println(s.Pop())
}
