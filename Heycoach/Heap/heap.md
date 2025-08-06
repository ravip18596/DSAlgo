# Heap

## Build heap

>Given an unsorted array, convert it into a heap.

$$ Time-Complexity: n/2 O(log n) => O(nlogn) $$

### Optimised Solution

$$ Time-Complexity: O(n) $$

```python
# Time Complexity: O(logn)
def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Time Complexity: O(n)
def buildHeap(arr, n):
    for i in range(n//2, -1, -1):
        max_heapify(arr, n, i)
    return arr

# Time complexity: O(logn)
def extractMax(arr, n):
    if n < 1:
        return None
    if n == 1:
        return arr.pop()
    root = arr[0]
    arr[0] = arr.pop()
    max_heapify(arr, n-1, 0)
    return root
```

## kth largest element

### Solution 1: sorting
- Time Complexity: O(nlogn)
- Space Complexity: O(1)

```python
def kthLargest(arr, k):
    arr.sort()
    return arr[-k]
```

### Solution 2: Heap

1. Build max heap: O(n)
2. Extract max k times : O(klogn)

- Time Complexity: O(n + klogn) 
- Space Complexity: O(n)

```python
# Time Complexity: O(logn)
def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Time Complexity: O(n)
def buildHeap(arr, n):
    for i in range(n//2, -1, -1):
        max_heapify(arr, n, i)
    return arr

# Time complexity: O(logn)
def extractMax(arr, n):
    if n < 1:
        return None
    if n == 1:
        return arr.pop()
    root = arr[0]
    arr[0] = arr.pop()
    max_heapify(arr, n-1, 0)
    return root

# Time complexity: O(klogn)
def kthLargest(arr, k):
    buildHeap(arr, len(arr))
    for i in range(k-1):
        extractMax(arr, len(arr))
    return arr[0]
```

### Solution 3: Priority Queue

- Time Complexity: O(nlogk)
- Space Complexity: O(k)

```python
import heapq

def kthLargest(arr, k):
    pq = []
    for i in range(k):
        heapq.heappush(pq, arr[i])

    for i in range(k, len(arr)):
        if arr[i] > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, arr[i])
    return pq[0]
```

## Top k frequent elements

- Time Complexity: O(nlogk)
- Space Complexity: O(k)

```python
import heapq

def topKFrequent(arr, k):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    pq = []
    for key, value in freq.items():
        heapq.heappush(pq, (value, key))
        if len(pq) > k:
            heapq.heappop(pq)
    res = []
    while pq:
        res.append(heapq.heappop(pq)[1])
    return res[::-1]
```

## Ugly Number II
[https://leetcode.com/problems/ugly-number-ii/description/](https://leetcode.com/problems/ugly-number-ii/description/)

> 1 is a ugly number. It is a special case.

```python
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        data = [1]
        heapq.heapify(data)
        s = set() # to track which elements are already in your heap
        s.add(1)
        count = 0
        while count < n-1:
            x = heapq.heappop(data)
            if x*2 not in s:
                s.add(x*2)
                heapq.heappush(data, x*2)
            if x*3 not in s:
                s.add(x*3)
                heapq.heappush(data, x*3)
            if x*5 not in s:
                s.add(x*5)
                heapq.heappush(data, x*5)
            count += 1

        return heapq.heappop(data)    
```


## Median of a data stream

[https://leetcode.com/problems/find-median-from-data-stream/description/](https://leetcode.com/problems/find-median-from-data-stream/description/)

$$ Time-Complexity:addNum:O(logn)$$
$$ Time-Complexity:findMedian:O(1)$$
$$ Space-Complexity:O(n)$$

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.median = 0.
        
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -1*num)
        elif num <= self.median:
            heapq.heappush(self.max_heap, -1*num)
            if len(self.max_heap) - len(self.min_heap) > 1:
                heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
        elif num > self.median:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) - len(self.max_heap) > 0:
                heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
        
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            self.median = -1*self.max_heap[0]
        else:
            max1 = -1*self.max_heap[0]
            min1 = self.min_heap[0]
            self.median = (max1 + min1)/2.0
        #print(self.max_heap, self.min_heap, self.median)
           
    def findMedian(self) -> float:
        return self.median
```



