Problem
-------
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.

Example
-------

Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.

Solution
--------

Most optimal Solution

- Time Complexity: O(n)
- Space Complexity: O(1)

```python
def bulb_on(A):
    ans = 0
    right = 0
    n = len(A)
    for i in range(n):
        right = max(right, A[i])
        if right == i+1:
            ans +=1
            
    return ans
    
if __name__ == '__main__':
    A=[1, 3, 4, 2, 5]
    print(bulb_on(A))
```