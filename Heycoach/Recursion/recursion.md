# Recursion

## Exponentiation

$$ T(N) = T(N-1) + O(1) $$ 
$$ Time-Complexity: O(N) $$

```python
def exp(a, n):
    if n==0:
        return 1
    return a * exp(a, n-1)
```

## Binary Exponentiation

$$ Time-Complexity: O(N) $$

$$ T(N) = 2*T(N/2) + O(1) $$

```python
def binexp(a, n):
    if n==0:
        return 1
    
    if n&1 == 1:
        # odd
        return binexp(a, (n-1)//2) * binexp(a, (n-1)//2)
    else:
        # even
        return binexp(a, n//2) * binexp(a, n//2)
```

$$ Time-Complexity: O(logN) $$
$$ T(N) = T(N/2) + O(1) $$

```python
def binexp(a, n):
    if n==0:
        return 1

    if n&1 == 1:
        temp = binexp(a, (n-1)//2)
        return temp * temp
    else:
        temp = binexp(a, n//2)
        return temp * temp
```

## Binary Search

$$ T(N) = T(N/2) + O(1) $$
$$ Time-Complexity: O(logN) $$

```python
def binary_search(arr: List[int], l: int, r: int, target: int) -> int:
    if l > r:
        return -1

    mid = (l+r)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid+1, r, target)
    else:
        return binary_search(arr, l, mid-1, target)
```

## Is subsequence

```python    
def is_subsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False

    if s[0] == t[0]:
        return is_subsequence(s[1:], t[1:])
    else:
        return is_subsequence(s, t[1:])
```

## Generate Paranthesis

$$ Time-Complexity: O(exponential) $$

> (x)y => x and y are well formed paranthesis

```python
def generate_paranthesis(n):
    if n == 0:
        return [""]

    result = []
    for i in range(n):
        for left in generate_paranthesis(i):
            for right in generate_paranthesis(n-i-1):
                result.append("(" + left + ")" + right)

    return result
```
