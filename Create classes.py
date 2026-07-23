class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def dissplay_books(self):
        for book in self.books:
            print(book)
library=Library()

library.add_book("Sahara")
library.add_book("Aleppo")
library.add_book("summer in tangier")
library.dissplay_books()