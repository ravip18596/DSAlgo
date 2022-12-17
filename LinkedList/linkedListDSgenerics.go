package main

import "fmt"

type Node[T any] struct {
	next *Node[T]
	val  T
}

func CreateNode[T any](val T) *Node[T] {
	return &Node[T]{val: val, next: nil}
}

func findEleInLL[T comparable](head *Node[T], target T) bool {
	temp := head
	for temp != nil {
		if temp.val == target {
			return true
		}
		temp = temp.next
	}
	return false
}

func (head *Node[T]) printLL() {
	temp := head
	for temp != nil {
		fmt.Print(temp.val, "->")
		temp = temp.next
	}
	fmt.Println()
}

func main() {
	head := CreateNode(1)
	head.next = CreateNode(2)
	head.next.next = CreateNode(3)
	head.printLL()
	fmt.Println(findEleInLL(head, 2))
	fmt.Println(findEleInLL(head, 4))
}
