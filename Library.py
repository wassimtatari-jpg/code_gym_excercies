class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def __str__(self):
        return f"Library with  books : {len(self.books)} "+",".join(self.books)
    def __len__(self):
        return len(self.books)
library=Library()

library.add_book("Romantice couple")
library.add_book("Summer and winter")
library.add_book("NO!!")

print(library)
print(f"Library with {len(library)} books")





        