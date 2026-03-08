from book import Book

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)

    def show_books(self):
        for book in self.books:
            print(book.get_info())