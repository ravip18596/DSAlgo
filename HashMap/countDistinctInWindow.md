# Problem

Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.

Example 2:

Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1

# Solution

```python
# [ 1, 2, 1, 3, 4, 2, 3]
#   0  1  2  3  4  5  6
#  since K = 4, create map for index 0->3
#  then update map for window index 1->4,2->5,3->6  
def countDistinct(self, A, N, K):
    # Code here
    m = {}
    for i in range(K):
        if A[i] in m:
            m[A[i]] += 1
        else:
            m[A[i]] = 1
    
    result = [len(m)]
    i = K
    while i<N:
        # updating map for ele left of current window
        if m[A[i-K]] <= 1:
            del m[A[i-K]]
        else:
            m[A[i-K]] -= 1
            
        # updating map for new element in current window
        if A[i] in m:
            m[A[i]] += 1
        else:
            m[A[i]] = 1
            
        result.append(len(m))
        i+=1
        
    return result
```