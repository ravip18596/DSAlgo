Classes and Objects
-------------------

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print('The car is starting...')
    
    def drive(self):
        print('The car is driving...')
        
    def stop(self):
        print('The car is stopping...')
    
        
if __name__ == '__main__':
    car = Car("Toyata", "Camry", 2014)
    car.start()
    car.drive()
    car.stop()
```

Inheritance
-----------

Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass)

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('The car is starting...')

    def drive(self):
        print('The car is driving...')

    def stop(self):
        print('The car is stopping...')


# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print('The car is charging...')


if __name__ == '__main__':
    my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
    my_electric_car.start()
    my_electric_car.drive()
    my_electric_car.stop()
    my_electric_car.charge()
```

Encapsulation
--------------
Encapsulation in python is achieved by making attributes private and accessing or modifying them using public methods (getter and setters)

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 0 <= age <= 120:
            self._age = age
        else:
            print("Invalid age")

            
if __name__ == '__main__':
    person = Person("Ravi", 28)
    print(person.get_name())
    print(person.get_age())
    person.set_age(30)
    print(person.get_age())
```

Polymorphism
-------------

Polymorphism allows objects of different classes can behave as object of a common superclass

```python
# Polymorphism
class Animal:
    def make_sound(self):
        print('Some generic Animal Sound')


class Dog(Animal):
    def make_sound(self):
        print('Bark!')


class Cat(Animal):
    def make_sound1(self):
        print('Meow!')

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.make_sound()
    cat.make_sound()
```

Abstraction
-----------

```python
# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

if __name__ == '__main__':
    circle = Circle(2)
    rectangle = Rectangle(2, 3)
    print(f'Area of circle is {circle.area()}')
    print(f'Area of rectangle is {rectangle.area()}')
```

Aggregation
-----------

Aggregation in python represents a "has-a" relationship where one class contains references to objects of another class
```python
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

if __name__ == '__main__':
    library = Library()
    library.add_book(Book("Book1"))
    library.add_book(Book("Book2"))
    for book in library.books:
        print(book.title)
```

Composition
-----------

Composition in python also represents a "has-a" relationship, but the lifecycle of contained object is tied to the container object

```python
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Bedroom")]

if __name__ == '__main__':
    house = House()
    for room in house.rooms:
        print(room.name)
```