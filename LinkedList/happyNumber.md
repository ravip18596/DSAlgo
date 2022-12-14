Solution
--------

- Approach 1: Detect Cycles with a HashSet
- Time  logN
- Space: logN


Approach 2: Detect cycle using Floyd cycle algo

Time: 
Space: 

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def sqSumDigit(n):
            sumV = 0
            while n>0:
                sumV += (n%10)*(n%10)
                n = n // 10
            return sumV

        slow, fast = sqSumDigit(n), sqSumDigit(sqSumDigit(n))
        while slow != fast:
            slow = sqSumDigit(slow)
            fast = sqSumDigit(sqSumDigit(fast))
            

        # if there is a cycle we reach here 
        return True if slow == 1 else False
```
