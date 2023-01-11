# Problem

Given an array, find largest 3 element in array

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23

# Solution

```python
arr = [10, 4, 3, 50, 23, 90]

first, second, third = arr[0], None, None
n = len(arr)

for i in range(1, n):
    if arr[i] > first:
        first = arr[i]
        second = first
        third = second
    elif arr[i] > second and first != arr[i]:
        second = arr[i]
        third = second
    elif arr[i] > third and second != arr[i]:
        third = arr[i]

print(f'first:{first}, second:{second}, third:{third}')
```