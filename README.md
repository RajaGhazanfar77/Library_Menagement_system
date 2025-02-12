# Simple Library Management System

This Python script implements a basic library management system. It allows users to add books, view available books, borrow and return books, and search for books by title, author, or genre.  The data is stored in-memory using lists, so it is not persistent across program executions.

## Features

* **Add Book:** Add new book information to the library, including ID, title, author, and genre.  Books are initially marked as "Available".
* **View Books:** Display a list of all books in the library with their details (ID, Title, Author, Genre, Status).
* **Borrow Book:** Allow a user to borrow a book by providing the book ID.  The book's status is updated to "Checked Out", and the book is associated with the user.
* **Return Book:** Allow a user to return a borrowed book by providing the book ID. The book's status is updated to "Available", and it is removed from the user's borrowed books list.
* **Search Books:** Search for books by title, author, or genre (case-insensitive).
* **User Management (Basic):**  While users aren't explicitly created, the borrow and return functions require a `user_id` to track which user has borrowed which book.  This is a simplified approach.

## Technologies Used

* Python

## How to Run

1.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `library.py`).
2.  **Run from Terminal:** Open a terminal or command prompt and navigate to the directory where you saved the file.
3.  **Execute:** Run the script using the command: `python library.py`

## How to Use

Once the script is running, you'll be presented with a menu:

1.  **Add Book:** Enter `1` and follow the prompts to add a new book.
2.  **View Books:** Enter `2` to see a list of all books.
3.  **Borrow Book:** Enter `3`, enter the `user_id` and then the `book_id` of the book you want to borrow.
4.  **Return Book:** Enter `4`, enter the `user_id` and then the `book_id` of the book you want to return.
5.  **Search Books:** Enter `5` and enter the search term.
6.  **Exit:** Enter `6` to quit the program.

## Data Storage

Currently, the book and user data is stored in lists within the script.  This means that the data is lost when the program terminates.

## Future Enhancements

* **Persistent Storage:** Implement a way to store data permanently, such as using a file (e.g., CSV, JSON) or a database.
* **User Management:** Implement proper user registration and login functionality.
* **Input Validation:** Add more robust input validation to handle invalid inputs gracefully.
* **Error Handling:** Implement better error handling to provide informative messages to the user.
* **Improved Search:** Allow for more complex search queries (e.g., searching by multiple criteria).
* **User Interface:** Consider using a graphical user interface (GUI) library like Tkinter, PyQt, or Kivy to create a more user-friendly interface.
* **Object-Oriented Design:** Refactor the code to use classes to represent books and users, improving code organization and maintainability.
