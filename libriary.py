from datetime import datetime


class Book:
    def __init__(self, title, author, isbn, publication_date, category):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.category = category

    def __str__(self):
        return f'{self.title} by {self.author}, published on {self.publication_date.year}. ISBN: {self.isbn}'


class FictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, category, genre):
        super().__init__(title, author, isbn, publication_date, category)
        self.genre = genre


class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, category, topic):
        super().__init__(title, author, isbn, publication_date, category)
        self.topic = topic


class ReferenceBook(Book):
    def __init__(self, title, author, isbn, publication_date, category, description):
        super().__init__(title, author, isbn, publication_date, category)
        self.description = description


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        if book not in self.collection:
            self.collection.append(book)

    def remove_book(self, book):
        if book in self.collection:
            self.collection.remove(book)

    def get_books_by_author(self, author):
        retl = []
        for b in self.collection:
            if b.author == author:
                retl.append(b)
        return retl

    def get_books_by_year(self, year):
        retl = []
        for b in self.collection:
            if b.publication_date.year == year:
                retl.append(b)
        return retl

    def get_books_by_category(self, category):
        retl = []
        for b in self.collection:
            if b.category == category:
                retl.append(b)
        return retl


# Testing objects:

book1 = FictionBook('Poirot\'s Early Cases', 'Agatha Christie', '9780008164843', datetime(2024, 1, 1), 'fictionbook',
                    'Detective')
book2 = NonFictionBook('A Political History of the World', 'Jonathan Holslag', '9780241395561', datetime(2019, 1, 1),
                       'nonfictionbook', 'History')
book3 = ReferenceBook('The Python Language Reference Manual', 'Guido van Rossum', '1906966141', datetime(2006, 11, 1),
                      'referencebook', 'Programming')

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for b in library.get_books_by_author('Guido van Rossum'):
    print(b)
for b in library.get_books_by_year(2019):
    print(b)
for b in library.get_books_by_category('fictionbook'):
    print(b)
