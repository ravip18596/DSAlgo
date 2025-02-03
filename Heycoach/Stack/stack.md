# Stack

## Monotonic Stack

### NGE (Next Greater Element)

[https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1](https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1)

maintain a monotonic decreasing stack

```python
def nextLargerElement(arr):
    # code here
    # monotonic decreasing stack
    stack = []
    nge = [-1]*len(arr)
    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[-1]] < arr[i]:
            j = stack.pop()
            nge[j] = arr[i]
        
        stack.append(i)
        
    return nge
```

### PGE (Previous Greater Element)

maintain a monotonic decreasing stack

```python
def prevGreaterElement(arr):
    n = len(arr)
    pge = [0]*n
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()

        if len(stack) == 0:
            pge[i] = -1
        else:
            pge[i] = stack[-1]

        stack.append(arr[i])
    
    return pge

arr = [ 10, 4, 2, 20, 40, 12, 30 ]
print(prevGreater(arr))
# Output [-1, 10, 4, -1, -1, 40, 40]
```

### NSE (Next smaller element)

maintain a monotonic increasing stack

```python
def nextSmallerElement(arr):
    n = len(arr)
    stack = []
    nse = [-1]*n
    for i in range(n):
        while len(stack) > 0 and arr[stack[-1]] > arr[i]:
            j = stack.pop()
            nse[j] = arr[i]

        stack.append(i)

    return nse

arr = [4, 8, 5, 2, 25]
print(nextSmallerElement(arr))
# Output: [2, 5, 2, -1, -1]
```

### PSE (Previous Smaller Element)

maintain a monotonic increasing stack

```python
def prevSmallerElement(arr):
    n = len(arr)
    pse = [0]*n
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] > arr[i]:
            stack.pop()

        if len(stack) == 0:
            pse[i] = -1
        else:
            pse[i] = stack[-1]

        stack.append(arr[i])

    return pse

arr = [2, 3, 4, 5, 1]
print(prevSmallerElement(arr))
# Output [-1 2 3 4 -1]
```
