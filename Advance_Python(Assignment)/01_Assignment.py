class Book:
    def __init__(self, code, name, writer):
        self.code = code
        self.name = name
        self.writer = writer
        self.is_available = True


class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.issued_books = []


class LibrarySystem:
    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_new_book(self, book):
        self.book_list.append(book)
        print(f"'{book.name}' added to the library.")

    def add_member(self, member):
        self.member_list.append(member)
        print(f"Member '{member.member_name}' registered.")

    def issue_book(self, member_id, book_code):
        member = next((m for m in self.member_list if m.member_id == member_id), None)
        book = next((b for b in self.book_list if b.code == book_code), None)

        if member is None:
            print("Member does not exist.")
            return

        if book is None:
            print("Book not found.")
            return

        if not book.is_available:
            print("Sorry! This book is already issued.")
            return

        book.is_available = False
        member.issued_books.append(book)
        print(f"{member.member_name} has borrowed '{book.name}'.")

    def submit_book(self, member_id, book_code):
        member = next((m for m in self.member_list if m.member_id == member_id), None)

        if member is None:
            print("Member does not exist.")
            return

        for book in member.issued_books:
            if book.code == book_code:
                book.is_available = True
                member.issued_books.remove(book)
                print(f"{member.member_name} returned '{book.name}'.")
                return

        print("This member has not borrowed the selected book.")

    def display_books(self):
        print("\n------ Library Catalogue ------")
        for book in self.book_list:
            state = "Available" if book.is_available else "Issued"
            print(f"Book ID : {book.code}")
            print(f"Title   : {book.name}")
            print(f"Author  : {book.writer}")
            print(f"Status  : {state}")
            print("-" * 30)


# ---------------- Main Program ----------------

library = LibrarySystem()

library.add_new_book(Book(201, "Programming in Python", "Mark Lee"))
library.add_new_book(Book(202, "Database Systems", "Thomas"))
library.add_new_book(Book(203, "Artificial Intelligence", "Peter Norvig"))

library.add_member(Member(1, "Aman"))
library.add_member(Member(2, "Sneha"))

library.display_books()

print("\nIssuing Book")
library.issue_book(1, 201)

library.display_books()

print("\nReturning Book")
library.submit_book(1, 201)

library.display_books()


# output:

# ------ Library Catalogue ------
# Book ID : 201
# Title   : Programming in Python
# Author  : Mark Lee
# Status  : Available
# ------------------------------
# Book ID : 202
# Title   : Database Systems
# Author  : Thomas
# Status  : Available
# ------------------------------
# Book ID : 203
# Title   : Artificial Intelligence
# Author  : Peter Norvig
# Status  : Available
# ------------------------------

# Issuing Book
# Aman has borrowed 'Programming in Python'.

# ------ Library Catalogue ------
# Book ID : 201
# Title   : Programming in Python
# Author  : Mark Lee
# Status  : Issued
# ------------------------------
# Book ID : 202
# Title   : Database Systems
# Author  : Thomas
# Status  : Available
# ------------------------------
# Book ID : 203
# Title   : Artificial Intelligence
# Author  : Peter Norvig
# Status  : Available
# ------------------------------

# Returning Book
# Aman returned 'Programming in Python'.

# ------ Library Catalogue ------
# Book ID : 201
# Title   : Programming in Python
# Author  : Mark Lee
# Status  : Available
# ------------------------------
# Book ID : 202
# Title   : Database Systems
# Author  : Thomas
# Status  : Available
# ------------------------------
# Book ID : 203
# Title   : Artificial Intelligence
# Author  : Peter Norvig
# Status  : Available
# ------------------------------