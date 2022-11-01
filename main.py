from Client import Client
from Book import Book

# declaration of clients list and make 3 instance
from Libarian import Librarian

clients = [
    Client(1, "Bahaa Salha", 20, "125874963", "12587963"),
    Client(2, "Mohamed", 12, "125874963", "12587963"),
    Client(3, "khaled", 80, "125874963", "12587963"),
]

# declaration of books list and make 4 instance
books = [
    Book(0, "he", "this is dummy data", "mohammed sh.", "active"),
    Book(1, "be", "this is dummy data", "ahmed sh.", "inactive"),
    Book(2, "she.", "this is dummy data", "mohanned sh.", "inactive"),
    Book(3, "key", "this is dummy data", "hamza sh.", "active"),
]

# declaration of librarian list to be available to initialization the values
librarians = []

# declaration of borrowed_orders list to be available to initialization the values
borrowed_orders: Book = []

# declaration variables to put in it the result of calculations
total_borrowed_books = 0
total_available_books = 0
total_borrowed_order = 0

# this loop to initial book that will be activated to borrowed_orders list
# and we get this books from books list after making if condition that filtering borrowed books
for i in range(len(books)):
    if books[i].status == "active":
        borrowed_orders.append(books[i])

# this loop to initial integer value to total_borrowed_books that calculated after knowing number of activated books
for i in range(len(books)):
    if books[i].status.__eq__("active"):
        total_borrowed_books = total_borrowed_books + 1

# this loop to initial integer value to total_borrowed_books that calculated after knowing number of inactivated books
for i in range(len(books)):
    if books[i].status.__eq__("inactive"):
        total_available_books = total_available_books + 1

# this variable to know length of borrowed_orders
total_borrowed_order = len(borrowed_orders)

# require 1
# create a new client and add it to the clients list...
Client(5, "momen", 50, "598774", "12549")

# require 2
# create a new librarian and add it to the librarian list...
librarians.append(Librarian(0, "moh", 20,  "05984166", 2000))

# require 3
# Create more than 4 books and add them to the book's list
books.append(Book(5, "le", "this is dummy data", "sohaib sh.", "active")),
books.append(Book(6, "iee", "this is dummy data", "fakhry sh.", "inactive"))
books.append(Book(7, "ke", "this is dummy data", "fakhry sh.", "inactive"))
books.append(Book(8, "ve", "this is dummy data", "fakhry sh.", "inactive"))

# require 4, 5, 6
# 4 Ask System to borrow a book
ask_system_to_borrow = str(input("ask the system"))
print("we have books")

# 5
# The system will ask you which book you want to borrow
# declare variables to take from user a value
book_title = str(input("which book you want to borrow"))

# 6  Checkbook status, Check if the box is active for borrowing or not
# this to check book_title that we  know the book allowed or not allowed
for i in range(len(borrowed_orders)):
    if borrowed_orders[i].title.__eq__(book_title):
        # the system ask user about info (id_no)
        # require 7
        # declare var ask about id_no
        user_id = int(input("enter your id"))
        # require 8
        # System will check if the client exists in the system or not
        for i in range(len(clients)):
            if clients[i].id == user_id:
                # If it exists System will create a borrow_order with the selected book and the selected client
                borrowed_orders.append(Book(user_id, book_title, "this is dummy data", "mohammed sh.", "active"))
            else:
                # required 10
                # Return book will be like that the client enters borrowing_id to the librarian to return it...
                liked_book = []
                liked_book.append(book_title)
                print("You are not allowed to borrow the book")
                print("the books you liked it",liked_book)
                break



# to print the information we need
print("total borrowed books: ", total_borrowed_books)
print("total available books: ", total_available_books)
print("total borrowed order: ", total_borrowed_order)
