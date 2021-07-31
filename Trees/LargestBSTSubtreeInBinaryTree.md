Problem
-------
Given a Binary Tree, write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST).
If the complete Binary Tree is BST, then return the size of the whole tree.

Solution
--------
- Time O(N)
- Space O(height of the tree)


```go
package main

type TreeNode struct {
	val         int
	left, right *TreeNode
}

func maxSizeBSTSubtree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	_, size := util(root, int(1e9), -int(1e9))
	return size
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func util(root *TreeNode, maxLeftBst, minRightBst int) (bool, int) {
	if root == nil {
		return true, 0
	}
	if root.left == nil && root.right == nil {
		return true, 1
	}
	leftBst, lsize := util(root.left, root.val, minRightBst)
	rightBst, rsize := util(root.right, maxLeftBst, root.val)

	if leftBst && rightBst && root.val > maxLeftBst && root.val < minRightBst {
		return true, lsize + rsize + 1
	} else {
		return false, max(lsize, rsize) + 1
	}
}
```