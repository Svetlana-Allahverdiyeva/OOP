from book import *
from student import *
from library import *


library = Library("City Library")

book1 = Book(1, "Clean Code", "Robert Martin", 464)
book2 = Book(2, "Python Crash Course", "Eric Matthes", 560)
book3 = Book(3, "Atomic Habits", "James Clear", 320)

student1 = Student(1, "Taleh")
student2 = Student(2, "Ramiz")
student3 = Student(3, "Ramal")


library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

library.addStudent(student1)
library.addStudent(student2)
library.addStudent(student3)


while True:

    print("""
    ===== LIBRARY MENU =====

    1. Show Books
    2. Show Students
    3. Search Book
    4. Search Student
    5. Borrow Book
    6. Return Book
    0. Exit

    ========================
    """)

    try:
        choice = input("Choose an option: ")

        if choice == "1":
            library.showBooks()

        elif choice == "2":
            library.showStudents()

        elif choice == "3":
            bookID = int(input("Enter Book ID: "))
            book = library.searchBook(bookID)

            if book:
                book.showInfo()

        elif choice == "4":
            studentID = int(input("Enter Student ID: "))
            student = library.searchStudent(studentID)

            if student:
                student.showInfo()

        elif choice == "5":
            studentID = int(input("Enter Student ID: "))
            bookID = int(input("Enter Book ID: "))

            library.borrowBook(studentID, bookID)

        elif choice == "6":
            studentID = int(input("Enter Student ID: "))
            bookID = int(input("Enter Book ID: "))

            library.returnBook(studentID, bookID)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")