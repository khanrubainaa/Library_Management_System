class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)
        self.books.append(book)

        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nLibrary Books:")

            for book in self.books:
                status = "Issued" if book.is_issued else "Available"

                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {status}")
                print("--------------------")

    def issue_book(self):
        title = input("Enter book title to issue: ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if book.is_issued:
                    print("Sorry! This book is already issued.")
                else:
                    book.is_issued = True
                    print("Book issued successfully!")

                return

        print("Book not found.")

    def return_book(self):
        title = input("Enter book title to return: ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

                return

        print("Book not found.")

    def run(self):
        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Add Book")
            print("2. View Books")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.issue_book()

            elif choice == "4":
                self.return_book()

            elif choice == "5":
                print("Thank you for using the Library Management System!")
                break

            else:
                print("Invalid choice! Please try again.")

library = Library()
library.run()