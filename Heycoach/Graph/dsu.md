# Disjoint Set Union

```text
interface DSU
{
    store the sets
    find(u, v)
    merge(u, v)
}
```

1. Every disjoint set is represented / visualised as tree (parent - child relationship)
2. Every tree's root is also representative of that disjoint set
3. Parent of the root is the root itself

## Find Representative

$$Time-Complexity: O(h)$$

```python
def findrep(int u) -> int:
    if u == parent[u]:
        return u
    return findrep(parent[u])
```

## Find

$$Time-Complexity: O(h)$$

```python
def find(int u, int v) -> bool:
    rep_u = findrep(u)
    rep_v = findrep(v)
    return rep_u == rep_v
```

## Union or Merge

$$Time-Complexity: O(h)$$

```python
def merge(int u, int v) -> None:
    rep_u = findrep(u)
    rep_v = findrep(v)
    if rep_u == rep_v:
        return
    if rank[rep_u] > rank[rep_v]:
        parent[rep_v] = rep_u
    elif rank[rep_u] < rank[rep_v]:
        parent[rep_u] = rep_v
    else:
        parent[rep_v] = rep_u
        rank[rep_u] += 1
```

## Path Compression

Potentially reducing the height of the tree

$$Time-Complexity: O(1)$$

```python
def find_rep(u: int) -> int:
    if u == parent[u]:
        return u
    parent[u] = find_rep(parent[u])
    return parent[u]
```

## Union Find Class

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
```

## Longest Continuous Range

You are given an array of integers nums. Your task is to find the length of the longest continuous range of consecutive integers in the array.

You need to implement an algorithm that operates in linear time complexity O(n).

```text
Input:

nums = [10,4,5,20,1,3,2]
Output:

5
Explanation:
The longest consecutive sequence of elements is [1, 2, 3, 4,5], which has a length of 5.
```

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

class Solution:
     def longestConsecutiveRange(self, cards):
        uf = UnionFind()
        
        # Add each card to the Union-Find structure
        for card in set(cards):
            uf.add(card)
            # Union with the next consecutive number
            uf.add(card + 1)
            uf.union(card, card + 1)
    
        # Find the size of each component
        max_length = 0
        component_size = {}
    
        for card in set(cards):
            root = uf.find(card)
            if root in component_size:
                component_size[root] += 1
            else:
                component_size[root] = 1
    
        # The maximum size of any component is the answer
        max_length = max(component_size.values())
    
        return max_length
```
