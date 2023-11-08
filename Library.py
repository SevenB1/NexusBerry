#library class
#Attributes: Books
#Behavior:addbook(),displaybooks()
#Book class
#Attributes: Title,author,available
#Behavior:
#Member class
#Attributes:name, id, borrowed_books
#Behavior:borrow_book(), return_book(), list_borrowed_books()
class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available
    def __str__(self):
        availability = "Available" if self.available else "Not available"
        return f"Title:{self.title} | Author:{self.author} | Status:{availability}"

class Ebook:
    def __init__(self,title,author,format):
        super().__init__(title,author)
        self.format = format
    def __str__(self):
        availability = "Available" if self.available else "Not available"
        return f"Title:{self.title} | Author:{self.author} Format:{self.format} | Status:{availability}"


class Member:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed '{book.title}' by {book.author}")
        else:
            print(f"Sorry,'{book.title}' is not available")

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned '{book.title}' by {book.author}")
        else:
            print(f"{self.name} has no borrowed books")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has the following books")
            for book in self.borrowed_books:
                print(f"{book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books")



class Library:
    def __init__(self):
        self.books = []
        self.ebooks = []

    def add_book(self,book):
        if isinstance(book,Ebook):
            self.ebooks.append(book)
        else:
            self.books.append(book)

    def display_books(self):
        if self.books:
            print("Books Available in the library")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library")
        if self.ebooks:
            print("E-books available in the library")
            for ebook in self.ebooks:
                print(ebook)
        else:
            print("No e-books available in the library")


book1 = Book("The Great Gatsby","F.Scott Fitzgerald")
book2 = Book("To kill a Mockingbird","Harper Lee")
book3 = Book("1984","George Orwell")
# ebook1 = Ebook("Calculus-III","Rober Haytt","PDF")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# library.add_book(ebook1)

member1 = Member("Ahmad")

library.display_books()

# member1.borrow_book(book1)
# #
# member1.borrow_book(book3)
#
# library.display_books()
#
# member1.list_borrowed_books()

#Assignment:
#Search method include which will take an  argument title of the book or Author
#Are you a 1. Member or 2. Admin
#Enter the Pin
#1. List_Books
#2. Search_Bookbytitle(self, title) and SearchBookbyauthor(self,author)
#       1. Physical Book (hard copy)
#       2. Ebook
#           1. Search by Author
#           2. Search by title
#3.List_borrowed_books

#Admin Interface
#1. Add Books
#       prompt for title of the book, prompt for author of the book
#2. Borrow_book
#       prompt for the member name, prompt for the title of the book, search the book in the library books,
#       add the book int the member borrowed book list
#3. Return_book