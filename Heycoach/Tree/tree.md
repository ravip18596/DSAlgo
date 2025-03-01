# Tree

## Height of a Tree

> Number of edges along the path from root to the farthest leaf node.

$$ Time-Complexity: O(N) $$
$$ Space-Complexity: O(N) $$

```python
def height(root):
    if root is None:
        return -1

    lheight = height(root.left)
    rheight = height(root.right)
    return 1 + max(lheight, rheight)
```

> Number of vertexes along the path from root to the farthest leaf node.

$$ Time-Complexity: O(N) $$
$$ Space-Complexity: O(N) $$

```python
def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)
    return 1 + max(lheight, rheight)
```

## Balanced Tree

For every node x,
1. find left subtree height (hl)
2. find right subtree height (hr)

if for all nodes |hl - hr| <= 1 then tree is balanced
else unbalanced

$$ Time-Complexity: O(N^2) $$
$$ Space-Complexity: O(N) $$

```python
def isBalanced(root):
    if root is None:
        return True

    lheight = height(root.left)
    rheight = height(root.right)

    if abs(lheight - rheight) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)
```

>Optimised Solution

## Traversals

### Inorder Traversal

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
```

### Preorder Traversal

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left) 
    preorder(root.right)
```

### Postorder Traversal

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return
    postorder(root.left) 
    postorder(root.right)
    print(root.data)
```

## Same Tree

> Two trees are same if they have same structure and same values at each node.

$$ Time-Complexity: O(N) $$

```python
def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)
    
    return p.val == q.val and left and right
```
