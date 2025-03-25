# Binary Search Tree

## Insert in BST

```python
def insert(root, key):
    if not root:
        return TreeNode(key)
    if root.val > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

## Inorder Predecessor

element that will come just before the given element in the inorder traversal.

```python
def inOrderPredecessor(root, key):
    predecessor = None
    while root is not None:
        if root.val > key:
            root = root.left
        else:
            predecessor = root.val
            root = root.right
    return predecessor
```

## Inorder Successor

element that will come just after the given element in the inorder traversal.

```python
def inOrderSuccessor(root, key):
    successor = None
    while root is not None:
        if root.val < key:
            root = root.right
        else:
            successor = root.val
            root = root.left
    return successor
```

## Searching in BST

```python
def search(root, key):
    if not root:
        return None

    if root.val == key:
        return root
    elif root.val < key:
        search(root.right, key)
    else:
        search(root.left, key)
    return None
```

## Return minimum element in a BST

```python
def findMin(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val
```

## Return maximum element in a BST

```python
def findMax(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.val
```

## Level order traversal

```python
def levelOrder(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

## Convert sorted array to Binary Search Tree

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root
```
