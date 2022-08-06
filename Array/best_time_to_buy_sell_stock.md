Problem
-------
[https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Examples
--------

### Example 1:

- Input: prices = [7,1,5,3,6,4]
- Output: 5
- Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2:

- Input: prices = [7,6,4,3,1]
- Output: 0
- Explanation: In this case, no transactions are done and the max profit = 0.


Solution
-------
- The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm
- the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, 
- find a contiguous subarray giving maximum profit.
- If the difference falls below 0, reset it to zero.

### Python

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        n = len(prices)
        max_curr, max_so_far = 0, 0
        
        for i in range(1, n):
            max_curr += prices[i] - prices[i-1]
            max_curr = max(0, max_curr)
            max_so_far = max(max_curr, max_so_far)
            
        return max_so_far
```
