Problem
-------

Given a binary tree of N nodes, where every node value is a number. Find the sum of all the numbers which are formed from root to leaf paths.
```text
Input :      
           6                               
         /   \                          
        3     5                      
      /   \     \
     2    5      4             
        /  \                        
       7    4  

Output: 13997

Explanation :
There are 4 leaves, hence 4 root to leaf paths:
Path                      Number
6->3->2                   632
6->3->5->7                6357
6->3->5->4                6354
6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997
```

Solution
--------
Simple preorder traversal
- Time - O(NlogN)
- Space - O(1)
`Python`
```python
def util(root, path):
    if root == None:
        return 0
    if root.left == None and root.right==None:
        path.append(root.data)
        num = path[0]
        for i in path[1:]:
            num = num*10 + i
        return num
    
    return util(root.left, path+[root.data]) + util(root.right, path+[root.data])
    
    
def treePathSum(root):
    # Code here
    if root == None:
        return 0

    sumV = util(root, [])
    return sumV
```

### Optimal Solution
- Time - 0(N)
- Space - O(1)

```python
def util(root, num):
    if root == None:
        return 0
    num = num*10 + root.data
    if root.left == None and root.right==None:
        return num
    return util(root.left, num) + util(root.right, num)
    
    
def treePathSum(root):
    # Code here
    if root == None:
        return 0
    sumV = util(root, 0)
    return sumV
```
