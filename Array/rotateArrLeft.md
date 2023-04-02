Problem
-------

Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 

Solution
--------

- Time: O(N)
- Space: O(1)
Left rotate array elements by d
Intution

- Rotate elements in a[0:d]
- Rotate elements in a[d:n-1]
- Rotate elements in a[0:n-1]

```python
def rotateArr(self,arr: List[int],d:int,n:int):
    def reverse(a: List[int],s:int,e:int):
        while s<e:
            a[s],a[e] = a[e], a[s]
            s+=1
            e-=1
    
    d = d%n
    reverse(arr, 0 ,d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)
        
    return arr
```

- Using Temp array

```python
#Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(arr: List[int],d:int,n:int):
        d = d%n
        temp = arr[:d]
        for i in range(0,n-d):
            arr[i] = arr[i+d]
        j=0
        for i in range(n-d, n):
            arr[i] = temp[j]
            j+=1
        return arr
```