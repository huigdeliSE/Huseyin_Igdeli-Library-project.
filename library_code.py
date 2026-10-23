class Author:
    def __init__(self, author, name):
        self.author_id = author
        self.name = name
class Member:
    def __init__(self, member, name):
        self.member_id = member
        self.name = name
class Book: 
    def __init__(self, book, book_name):
        self.book = book
        self.book_name = book_name 
        
class Loan:
    def __init__(self, loan, book: Book, member: Member):
        self.loan = loan
        self.book = book
        self.member = member               
class Library:
    def __init__(self, name, book: Book, loan: Loan, member: Member):
        self.name = name
        self.Book = book
        self.Member = member
        self.loan = loan
my_library = Library("hüseyin","Dune",1,2)
print(my_library.loan)
print(my_library.Book)
print(my_library.name)