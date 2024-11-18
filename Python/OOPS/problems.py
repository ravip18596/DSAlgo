class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

    def get_horsepower(self):
        return self.horsepower

    def get_type(self):
        return self.type

class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def display_info(self):
        print(f'Car: {self.name} {self.model}, Engine: {self.engine.get_horsepower()} HP {self.engine.get_type()}')

def main1():
    engine1 = Engine(200, "V3")
    engine2 = Engine(400, "V6")

    car1 = Car("Ford", "Mustang", engine1)
    car2 = Car("Rolls Royce", "Phantom", engine2)

    car1.display_info()
    car2.display_info()


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Books by {self.name}")
        for book in self.books:
            print(book.get_title())

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        print('Library Books:')
        for book in self.books:
            print(f'{book.get_title()} by {book.get_author().name}')

def main2():
    author1 = Author('Arthur Conan Doyle')
    author2 = Author('George R.R. Martin')

    book1 = Book('Sherlock Holmes', author1)
    book2 = Book('Game of Thrones', author2)

    author1.add_books(book1)
    author2.add_books(book2)

    library = Library()
    library.add_book(book1)
    library.add_book(book2)

    library.list_books()
    print()
    author1.list_books()
    author2.list_books()


if __name__ == '__main__':
    main2()