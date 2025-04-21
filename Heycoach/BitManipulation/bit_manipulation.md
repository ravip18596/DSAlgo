# Bit Manipulation

## Given a number, find the kth digit

```python
def findKthDigit(n, k):
    return (a>>k-1)&1

def findKthDigit(n, k):
    return (1<<k-1)&n
```

## Total Set Bits
Given a positive integer N, find the total count of set bits for all numbers from 1 to N (both inclusive). A set bit is a binary digit that is set to 1.
```text
Input:

N = 4
Output:

 5
Explanation:
For numbers from 1 to 4.
For 1: 0 0 1 = 1 set bit
For 2: 0 1 0 = 1 set bit
For 3: 0 1 1 = 2 set bits
For 4: 1 0 0 = 1 set bit
For 4: 1 0 1 = 2 set bit
Therefore, the total set bits is 7.
```
```python
class Solution:
    def count_set_bit(self, N):
      #Write your code here
      offset = 1
      dp = [0]*(n+1)

      for i in range(1, n+1):
          if 2*offset == i:
              offset = i
          
          dp[i] = 1 + dp[i-offset]

      return sum(dp)
```

## Single Number

Given an array, all numbers appear twice except for one number which appears once. Determine that number

```python
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
```

## Single Number II

Given an array, all numbers appear thrice except for one number which appears once. Determine that number

```python
def singleNumber(nums):
    # Initialize an array to count bits
    bit_count = [0] * 32
    
    # Count the number of times each bit appears
    for num in nums:
        for i in range(32):
            if (num >> i) & 1:
                bit_count[i] += 1
    
    # Reconstruct the unique number
    result = 0
    for i in range(32):
        if bit_count[i] % 3 != 0:
            result |= (1 << i)
    
    # Handle negative numbers
    if bit_count[31] % 3 != 0:
        result -= (1 << 32)
    
    return result
```

## Single Number III

Given an array, all numbers appear twice and two numbers which appears once. Determine those numbers

```python
def singleNumber(nums):
    # Step 1: XOR all numbers to get the XOR of the two unique numbers
    xor_result = 0
    for num in nums:
        xor_result ^= num
    
    # Step 2: Find a set bit (rightmost set bit)
    set_bit = xor_result & -xor_result
    
    # Step 3: Initialize the two unique numbers
    num1 = 0
    num2 = 0
    
    # Step 4: Partition the numbers into two groups and XOR them
    for num in nums:
        if (num & set_bit) == 0:
            num1 ^= num  # Group with the set bit
        else:
            num2 ^= num  # Group without the set bit
    
    return num1, num2

# Example usage:
arr = [4, 5, 6, 7, 4, 5]
print(singleNumber(arr))  # Output: (6, 7) or (7, 6)
```
