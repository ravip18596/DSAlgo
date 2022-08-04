powerful generalized binary search template
--------------------------------------------
Binary Search helps us reduce the search time from linear O(n) to logarithmic O(log n). But when it comes to implementation, it's rather difficult to write a bug-free code in just a few minutes.   
Some of the most common problems include:

- When to exit the loop? Should we use left < right or left <= right as the while loop condition?
- How to initialize the boundary variable left and right?
- How to update the boundary? How to choose the appropriate combination from left = mid, left = mid + 1 and right = mid, right = mid - 1?


### Template 

Minimize target , start condition(k) is True
```python
def binary_search(arr) -> int:
    def condition(value) -> bool:
        pass
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right-left)//2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
        
    return left
```

### Problem 1

Basic Application
278. First Bad Version [Easy]

You are a product manager and currently leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which will return whether version is bad.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

### Solution

First, we initialize left = 1 and right = n to include all possible values. Then we notice that we don't even need to design the condition function. It's already given by the isBadVersion API. Finding the first bad version is equivalent to finding the minimal k satisfying isBadVersion(k) is True. Our template can fit in very nicely

```python
def fist_defective_version(n):
    left, right = 1, n
    while left < right:
        mid = left + (right-left)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

### Problem

69. Sqrt(x) [Easy]

Implement int sqrt(int x). Compute and return the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example:

Input: 4
Output: 2

Input: 8
Output: 2

### Solution

We need to search for maximal k satisfying k^2 <= x
```python
def sqrt(x: int):
    left, right = 0, x
    while left < right:
        mid = left + (right-left)//2
        if mid*mid > x:
            right = mid
        else:
            left = mid+1
    return left-1
```

### Problem

[BinarySearch/insertMissingNumber](../BinarySearch/insertMissingNumber.md)

### Solution

Notice that the input target might be larger than all elements in nums and therefore needs to placed at the end of the array. That's why we should initialize right = len(nums) instead of right = len(nums) - 1.


```python
def searchIndex(nums, target) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left
```

## Advanced Problems


