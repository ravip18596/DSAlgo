Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
```text
Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

`Solution`

```cgo
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        r(root,ans,0);
        return ans;
    }
    void r(TreeNode *root,vector<int>& v,int depth)
    {
        if(root==NULL){
            return;
        }
        if(depth==v.size()){
            v.push_back(root->val);
        }
        r(root->right,v,depth+1);
        r(root->left,v,depth+1);
    }
};
```