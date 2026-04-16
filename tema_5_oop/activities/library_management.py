class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    name: str
    books: list[Book] = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def remove_book(self, isbn: str) -> None:
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break
        print(f"Removed book with ISBN {isbn} from the library.")
    
    def list_books(self) -> None:
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

# Example usage
the_greatest_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
to_kill_a_mockingbird = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
library = Library("City Library")

print("Should indicate no books in the library:")
library.list_books()

library.add_book(the_greatest_gatsby)
library.add_book(to_kill_a_mockingbird)

print("\nShould list the added books:")
library.list_books()

print("\nRemoving 'The Great Gatsby' from the library...")
library.remove_book("978-0743273565")

print("\nShould list the remaining books:")
library.list_books()



