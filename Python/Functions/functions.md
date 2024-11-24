Closures
--------

Closures is a function object that remembers values in enclosing scopes even if they are not present in memory. 

```python
def outer_function(x):
    def inner_function(y):
       return x + y
    return inner_function


if __name__ == '__main__':
    func = outer_function(5)
    print(func(3))
```

Decorators
-----------

- Decorators allows you to add functionality to existing functions dynamically
- They are functions themselves and wrap themselves around other functions and modify their behaviour.

```python
def decorator(func):
    def wrapper():
        print('Before executing function')
        func()
        print('After executing function')

    return wrapper

@decorator
def say_hello():
    print('Hello!...')

if __name__ == '__main__':
    say_hello()
```

Generator Functions
-------------------
- Generator functions allows you to behave like an iterator.
- Instead of returning single value, they return a sequence of values using the yield keyword

```python
def countdown(n):
    while n>0:
        yield n
        n -= 1

    
if __name__ == '__main__':
    for i in countdown(5):
        print(i)
```

Inbuilt Functions
-----------------

## map

Applies a given function to all items in an input list and returns a new list containing the results

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
```

## filter

Returns an iterator yielding those items of an iterator for which the functions returns true

```python
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x%2==0, numbers)
print(list(evens))
```

## reduce

```python

```