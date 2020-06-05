
`Solution`

`GO`

```go
package main
type TreeNode struct {
 	Val int
 	Left *TreeNode
 	Right *TreeNode
}
func bstFromPreorder(preorder []int) *TreeNode {
    if len(preorder)==0{
        return nil
    }
    root := TreeNode{
        Val:preorder[0],
        Left:nil,
        Right:nil,
    }
    diff := 0
    for i:=0;i<len(preorder);i++{
        if preorder[0] >= preorder[i]{
            diff++
        }
    }
    //fmt.Println(preorder[1:diff],preorder[diff:])
    root.Left = bstFromPreorder(preorder[1:diff])
    root.Right = bstFromPreorder(preorder[diff:])
    return &root
}
```

`cpp`

```cgo
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        return util(preorder,0,preorder.size()-1);
    }
    
    TreeNode * util(vector<int>& preorder,int start, int end) {
        if (start>end || start > preorder.size()-1 || end > preorder.size()-1){
            return NULL;
        }
        TreeNode *root = new TreeNode(preorder[start]);
        int diff=start;
        while (diff<=end){
            if (preorder[diff]<=preorder[start]){
                diff++;
            }else{
                break;
            }
        }
        root->left = util(preorder,start+1,diff-1);
        root->right = util(preorder,diff,end);
        
        return root;
    }
};
```