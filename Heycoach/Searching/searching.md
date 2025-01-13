# Searching

### Sorted Array Search

You are given a sorted array arr containing distinct integers. Your task is to implement a function search_position that, given a target value, returns the index where the 
target is found in the array. If the target is not present, return the index where it would be if inserted in order.

```text
Input: arr = [1,3,5,6], target = 5
Output: 2
```

```text
Input: arr = [1,3,5,6], target = 2
Output: 1
```

```cpp
int search_position(vector<int>& arr, int target) {
        int l = 0;
        int r = arr.size();

        while(l < r)
        {
          int mid = (l+r)>>1;
          if(arr[mid] < target)
          {
            l = mid+1;
          }else{
            r = mid;
          }
        }
        return l; 
    }
```
## Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

## Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Upper Bound

Find the first element that is strictly greater than the target.

```python
def upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

### Lower Bound

Find the first element that is greater than or equal to the target.

```python
def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

### Find Peak Element

```python
def findPeakElement(nums: List[int]) -> int:
    """
    Time complexity: O(log n)
    """
    n = len(nums)
    if n==1:
        return 0

    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1

    l, r = 1, n-2
    while l<=r:
        mid = (l+r)>>1
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid

        if nums[mid] < nums[mid+1]:
            l = mid+1
        else:
            r = mid-1
```

### Square root

```python
    def square_root(self, n):
        #Write your code here
        left, right = 0, n
        while left <= right:
        mid = (left+right)//2
        if mid*mid == n:
          return mid
        if mid*mid > n:
          right = mid-1
        else:
          left = mid+1
        
        return left-1
```

### Find min in rotated sorted array

[find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

```python
def findMin(nums: List[int]) -> int:
    if nums[0] <= nums[-1]:
        return nums[0]
    
    left, right = 1, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] < nums[mid-1]:
            return nums[mid]
       
       if nums[mid] < nums[right]:
            right = mid-1
        else:
            left = mid+1

```

### Search in rotated sorted array

[search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

```python
def search(nums: List[int], target: int) -> int:
        i, n = 1, len(nums)
        while i<n and nums[i-1]<nums[i]:
            i+=1

        pivot = i

        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            rotated_mid = (mid+pivot)%n
            if nums[rotated_mid] == target:
                return rotated_mid
            elif nums[rotated_mid] < target:
                left = mid+1
            else:
                right = mid-1

        return -1
```


## Ternary Search


