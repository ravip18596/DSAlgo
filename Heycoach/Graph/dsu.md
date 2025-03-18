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
