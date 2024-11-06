books = []
users = []

def add_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author's name: ")
    genre = input("Enter genre: ")
    status = "Available"
    books.append({"ID": book_id, "Title": title, "Author": author, "Genre": genre, "Status": status})

def view_books():
    for book in books:
        print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")

def borrow_book(user_id):
    book_id = int(input("Enter book ID to borrow: "))
    for book in books:
        if book['ID'] == book_id and book['Status'] == "Available":
            book['Status'] = "Checked Out"
            for user in users:
                if user['ID'] == user_id:
                    user['Borrowed Books'].append(book)
            print("Book borrowed successfully!")
            return
    print("Book not found or not available.")

def return_book(user_id):
    book_id = int(input("Enter book ID to return: "))
    for user in users:
        if user['ID'] == user_id:
            for book in user['Borrowed Books']:
                if book['ID'] == book_id:
                    book['Status'] = "Available"
                    user['Borrowed Books'].remove(book)
                    print("Book returned successfully!")
                    return
    print("Book not found or not borrowed by this user.")

def search_books():
    search_term = input("Enter search term (title, author, or genre): ")
    results = [book for book in books if search_term.lower() in book['Title'].lower() or search_term.lower() in book['Author'].lower() or search_term.lower() in book['Genre'].lower()]
    for book in results:
        print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            user_id = int(input("Enter user ID: "))
            borrow_book(user_id)
        elif choice == 4:
            user_id = int(input("Enter user ID: "))
            return_book(user_id)
        elif choice == 5:
            search_books()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()