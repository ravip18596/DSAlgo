Problem
-------
```text
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.
```
Examples
--------
```text
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
target = 5, K = 2

Output: [7,4,1]
```
![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

Solution
--------
```text
Time  - O(N)
Space - O(N)
We first do a depth first search where we annotate every node with information about it's parent.
After, we do a breadth first search to find all nodes a distance K from the target.
```
```go
package main
type TreeNode struct {
      Val int
      Left *TreeNode
      Right *TreeNode
 }

func distanceK(root *TreeNode, target *TreeNode, K int) []int {
    if K==0{
        return []int{target.Val}
    }
    parentMap := make(map[*TreeNode]*TreeNode)
    dfs(root,parentMap,nil)
    //Now parentMap is set
    //and now bfs-level order traversal with left+right+parent nodes
    //in next level
    seenSet := make(map[*TreeNode]struct{})
    queue := make([]*TreeNode,0)
    queue = append(queue,target)
    queue = append(queue,nil)
    seenSet[target]=struct{}{}
    seenSet[nil]=struct{}{} //for nil nodes and parent of root

    var dist int
    for len(queue)>0{
        node := queue[0]
        queue = queue[1:]
        if node==nil{
            dist = dist+1
            if dist==K{
                var res []int
                for _,n:=range queue{
                    if n!=nil{
                        res = append(res,n.Val)
                    }
                }
                return res
            }
            if len(queue)>0{
                queue=append(queue,nil)
            }
        }else{
            if _,ok:=seenSet[node.Left];!ok{
                seenSet[node.Left]=struct{}{}
                queue = append(queue,node.Left)
            }
            if _,ok:=seenSet[node.Right];!ok{
                seenSet[node.Right]=struct{}{}
                queue = append(queue,node.Right)
            }
            
            if _,ok:=seenSet[parentMap[node]] ;!ok{
                seenSet[parentMap[node]]=struct{}{}
                queue = append(queue,parentMap[node])
            }  
            
        }
    }
    return []int{}
}

func dfs(root *TreeNode,parentMap map[*TreeNode]*TreeNode, parent *TreeNode){
    if root==nil{
        return
    }
    parentMap[root]=parent
    dfs(root.Left,parentMap,root)
    dfs(root.Right,parentMap,root)
}
```
