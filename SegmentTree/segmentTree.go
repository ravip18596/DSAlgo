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
type SegmentTree struct{
    tree []int
    arrlen int
}

func GetSegmentTree(arr []int) SegmentTree{
    s := SegmentTree{}
    n := len(arr)
    s.tree = make([]int,2*n)
    s.arrlen = n
    s.buildTree(arr)
    return s
}

/*
Time - O(N)
Space - O(2N) ~ O(N)
Bottom up Approach

*/
func (sg SegmentTree) buildTree(arr []int) {
    n := len(arr)
    for i:=n;i<2*n;i++{
        sg.tree[i] = arr[i-n]
    }
    for i:=n-1;i>0;i--{
      sg.tree[i] = sg.tree[i*2] + sg.tree[i*2+1]
    }
}

/*
Time - O(LogN) time required to rebuild the range sum (non-leaf nodes) anf logN levels
Space - O(1)
*/
func (sg *SegmentTree) Update(i, val int) {
   pos := i + sg.arrlen
   sg.tree[pos] = val
   for pos > 0{
       left,right := pos,pos
       if pos&1 == 0{ //even
           right = pos+1
       }else{
           left = pos-1
       }
       sg.tree[pos/2] = sg.tree[left] + sg.tree[right]
       pos = pos/2
   }
}
/*
l<=r and [L...l] and [r...R]
time - O(LogN)
space - O(1)
*/
func (sg *SegmentTree) RangeSumQuery(l,r int) int{
    var sum int
    // leaf node is accessible in segment tree by adding n
    l,r = l+sg.arrlen, r + sg.arrlen
    for l<=r{
        if l&1==1{ // left is odd
            sum += sg.tree[l]
            l++
        }
        if r&1==0{ // right is even
	    sum += sg.tree[r]
            r--
        }
        l /= 2
        r /= 2
    }
    return sum
}

func main() {
    arr := []int{5,2,3,4}
    s := GetSegmentTree(arr)
    fmt.Println("Initial Arr: ",arr)
    fmt.Println("arr into segment tree in array form: ",s.tree )
    s.Update(2,7)
    fmt.Println("Update arr[2] == 7. Segment tree: ",s.tree)
    s.Update(1,1)
    fmt.Println("Update arr[1] == 2. Segment tree: ",s.tree)
    sum := s.RangeSumQuery(1,3)
    fmt.Println("sum of arr from arr[1] to arr[3] is: ",sum)
    
}
