Problem
-------
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

Insights
--------
1) Max path can happen between two leaf node or between root and leaf node

### Approach 1: Distance with Heights

![Distance with heights](https://leetcode.com/problems/diameter-of-n-ary-tree/Figures/1522/1522_formula_depth.png)

Solution
--------

```text
Time Complexity - 
Space Complexity -
```

```go
type Node struct{
     Val int
     Children []*Node
}

func diameter(root *Node) {
    
}
```

