class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_taken = False

    def __str__(self):
        return f"\"{self.title}\" by {self.author}, ${self.price}"


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.books_read = 0
        self.books_with_human = []

    def take_book(self, library, book_title):
        book = library.give_book(book_title)
        if book:
            self.books_with_human.append(book)
            self.books_read += 1
            print(f'{self.name} has taken the book: {book}')

    def return_book(self, library, book_title):
        for book in self.books_with_human:
            if book.title == book_title:
                self.books_with_human.remove(book)
                library.return_book(book)
                print(f"{self.name} has returned the book: {book}")
                return
        print(f'{self.name} doesn\'t have the book titled \"{book_title}\".')

    def buy_book(self, library, book_title):
        book = library.sell_book(book_title)
        if book:
            self.books_with_human.append(book)
            print(f'{self.name} has bought the book: {book}')
        else:
            print(f'{self.name} couldn\'t buy the book titled \"{book_title}\".')

    def __str__(self):
        books_on_hand = len(self.books_with_human)
        return (f'{self.name}, {self.age} years old, {self.gender}. '
                f'Books read: {self.books_read}. '
                f'Books with {self.name}: {books_on_hand}')


class Library:
    def __init__(self):
        self.books = []
        self.taken_books = []
        self.records = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book to library: {book}")

    def give_book(self, book_title):
        for book in self.books:
            if book.title == book_title and not book.is_taken:
                book.is_taken = True
                self.taken_books.append(book)
                return book
        print(f'Book \"{book_title}\" is not available.')
        return None

    def return_book(self, book):
        book.is_taken = False
        self.taken_books.remove(book)

    def sell_book(self, book_title):
        for book in self.books:
            if book.title == book_title and not book.is_taken:
                self.books.remove(book)
                return book
        print(f"Book \"{book_title}\" is not available for sale.")
        return None

    def borrowed_books_info(self):
        if not self.records:
            print("No books borrowed yet.")
        for person, books in self.records.items():
            if books:
                print(f'{person.name} has borrowed the following books:')
                for book in books:
                    print(f'  - {book}')

    def __str__(self):
        total_books = len(self.books)
        books_taken = len(self.taken_books)
        return f"Library has {total_books} books. {books_taken} books are currently borrowed."

book1 = Book("1984", "George Orwell", 10)
book2 = Book('Brave New World', 'Aldous Huxley', 12)
book3 = Book("Fahrenheit 451", "Ray Bradbury", 8)
book4 = Book('The Catcher in the Rye', 'J.D. Salinger', 14)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

egor = Human('Egor', 16, 'male')
nikita = Human("Nikita", 18, "male")

egor.take_book(library, "1984")
egor.take_book(library, 'Brave New World')

nikita.take_book(library, 'Fahrenheit 451')
nikita.return_book(library, "Fahrenheit 451")

nikita.return_book(library, '1984')

nikita.buy_book(library, "The Catcher in the Rye")

egor.take_book(library, 'The Catcher in the Rye')

egor.buy_book(library, 'Brave New World')

print(egor)
print(nikita)
print(library)

egor.return_book(library, "1984")

print("Final library:")
print(library)
