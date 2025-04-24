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
