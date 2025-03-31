# Bit Manipulation

## Given a number, find the kth digit

```python
def findKthDigit(n, k):
    return (a>>k-1)&1

def findKthDigit(n, k):
    return (1<<k-1)&n
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
