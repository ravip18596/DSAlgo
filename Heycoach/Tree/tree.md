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

## Symmetric Tree

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def symmetricTree(q: Node, q: Node) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return p.data == q.data and symmetricTree(root.left) and symmetricTree(root.right)
```

## Invert a binary tree

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def invertTree(root) -> Node:
    if root is None:
        return root
    
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root 
```

## Binary Tree from inorder and postorder traversal

> Inorder Traversal is sorted in increasing order.

$$ Time-Complexity: O(N) $$

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = Node(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:mid], postorder[:mid])
    root.right = buildTree(inorder[mid + 1:], postorder[mid:])
    return root
```


## Binary Tree from inorder and preorder traversal

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def buildTree(inorder, preorder):
    if len(inorder) == 0:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(inorder[:mid], preorder[1:mid + 1])
    root.right = buildTree(inorder[mid + 1:], preorder[mid + 1:])
    return root
```

## Top View of a binary tree

1. use a breadth-first search (BFS) approach with a queue.
2. The idea is to keep track of the horizontal distance of each node from the root and store the first node encountered at each horizontal distance.

```python
class Solution:
  def topView(self, root):
    if not root:
      return []
    
    # This will store the first node at each horizontal distance
    top_view_map = {}
    # Queue for BFS: stores pairs of (node, horizontal_distance)
    queue = [(root, 0)]
    # Horizontal distance of the root is 0
    min_hd = 0
    max_hd = 0
    while queue:
      node, hd = queue.pop(0)
      # If this is the first time we are visiting this horizontal distance
      if hd not in top_view_map:
        top_view_map[hd] = node.val

      min_hd = min(min_hd, hd)
      max_hd = max(max_hd, hd)

      if node.left:
        queue.append((node.left, hd-1))
      if node.right:  
        queue.append((node.right, hd+1))

    return [top_view_map[hd] for hd in range(min_hd, max_hd+1)]
```
