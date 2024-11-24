def outer_function(x):
    def inner_function(y):
       return x + y
    return inner_function


def decorator(func):
    def wrapper():
        print('Before executing function')
        func()
        print('After executing function')

    return wrapper

@decorator
def say_hello():
    print('Hello!...')


def countdown(n):
    while n>0:
        yield n
        n -= 1


if __name__ == '__main__':
    func = outer_function(5)
    print(func(3))
    print()
    say_hello()
    print()
    for i in countdown(5):
        print(i)

    print()
    numbers = [1, 2, 3, 4, 5]
    squared = map(lambda x: x**2, numbers)
    print(list(squared))
    print()

    numbers = [1, 2, 3, 4, 5]
    evens = filter(lambda x: x%2==0, numbers)
    print(list(evens))


