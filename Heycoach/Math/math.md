# Math

## GCD

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

## Extended GCD (Eucliean Algorithm)

- Given a,b then GCD(a,b) is some linear combination of a,b
- GCD(a,b) = ax + by (where x,y are integers)


```python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
```

### Coefficient GCD

```python
def coeffGCD(r1, r2, x1, x2, y1, y2):
    if (r2==0):
        return x1, y1

    x3 = x1 - x2 * (r1 // r2)
    y3 = y1 - y2 * (r1 // r2)

    return coeffGCD(r2, r1 % r2, x2, x3, y2, y3)
```

## GCD of two numbers formed by n repeating x and y times

Problem
[GCD of two numbers formed by n repeating x and y times](https://www.geeksforgeeks.org/gcd-two-numbers-formed-n-repeating-x-y-times/)

```python
def gcd(a, b): 
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
# Prints Greatest Common Divisor of 
# number formed by n repeating x times 
# and y times. 
def findgcd(n, x, y): 
  
    # Finding GCD of x and y. 
    g = gcd(x, y) 
  
    # Print n, g times. 
    for i in range(g): 
        print(n) 
  
# Driver code 
n = 123
x = 5
y = 2
  
findgcd(n, x, y) 
```
