## Kth Smallest in BST

```python
def KthSmallestElement(self, root, K):
    #code here.
    def util(root, K , c):
        if root is None or c[0]>=K:
            return
        util(root.left, K, c)
        c[0]+=1
        if c[0]==K:
            c[1] = root.data
        util(root.right, K, c)

    # c[0] stores the counter var and c[1] stores the kth smallest result  
    c = [0, -1]
    util(root, K , c)
    return c[1]
```

## Kth Largest in BST

- reverse inorder

```python
def kthLargest(self,root, k):
    def util(root,k, c):
        if root is None or c[0]>=k:
            return
        
        util(root.right, k, c)
        c[0]+=1
        if c[0]==k:
            c[1] = root.data
            return
        
        util(root.left,k,c)

    c = [0, 0]
    util(root,k, c)
    return c[1]
```