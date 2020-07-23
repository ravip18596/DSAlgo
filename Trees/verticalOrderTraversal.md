```text
Given a binary tree, return the vertical order traversal of its nodes values.
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
```
![](https://assets.leetcode.com/uploads/2019/01/31/1236_example_1.PNG)
```
Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
```
![](https://assets.leetcode.com/uploads/2019/01/31/tree2.png)
```
Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
```

```go
package main
import "sort"
type TreeNode struct {
 	Val int
 	Left *TreeNode
 	Right *TreeNode
}
type Node struct{
    Depth int
    Val int
}
func verticalTraversal(root *TreeNode) [][]int {
    hashmap := make(map[int][]Node)
    vertTravUtil(root,hashmap,0,0)
    minkey := int(1e9)
    for key := range hashmap{
        if key<minkey{ minkey=key }
    }
    minkey *= -1
    result := make([][]int,len(hashmap))
    for key,val := range hashmap{
        sort.Slice(val,func(i,j int) bool{
            if val[i].Depth==val[j].Depth{
                return val[i].Val < val[j].Val
            }
            return val[i].Depth < val[j].Depth
        })
        for i:=0;i<len(val);i++{
            result[key+minkey] = append(result[key+minkey], val[i].Val)
        }
    }
    return result
}

func vertTravUtil(root *TreeNode,hashmap map[int][]Node,width,depth int){
    if root==nil{ return }
    hashmap[width] = append(hashmap[width],Node{Val:root.Val, Depth:depth})
    vertTravUtil(root.Left,hashmap,width-1,depth+1)
    vertTravUtil(root.Right,hashmap,width+1,depth+1)
}
```