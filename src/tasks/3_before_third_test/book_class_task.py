class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.borrowed_by: Borrower | None = None
        

    def show_info(self) -> None:
        if self.borrowed_by:
            status = f"Borrowed by borrowerID: {self.borrowed_by.borrower_id}"
        else:
            status = "Available"
            
        print(f"Title: {self.title} | Author: {self.author} | Status: {status}")
        

class Borrower:
    def __init__(self, borrower_id: str) -> None:
        self.borrower_id = borrower_id
        self.loaned_books = []
    
    def borrow_book(self, selected_book: Book) -> None:
        if selected_book.borrowed_by is None:
            selected_book.borrowed_by = self
            self.loaned_books.append(selected_book)
            print(f"Book {selected_book.title} is now borrowed by borrowerID: {self.borrower_id}")
        else:
            print(f"Book {selected_book.title} is already borrowed by borrowerID: {selected_book.borrowed_by.borrower_id}")

    
    def return_book(self, selected_book: Book) -> None:
        if selected_book in self.loaned_books:
            selected_book.borrowed_by = None
            self.loaned_books.remove(selected_book)
            print(f"Book {selected_book.title} has been returned")
        else:
            print(f"Book {selected_book.title} is not borrowed by borrowerID: {self.borrower_id}")
    
    def show_info(self) -> None:
        loaned_books = ", ".join(book.title for book in self.loaned_books) or "None"
        print(f"Borrower ID: {self.borrower_id} | Loaned books: {loaned_books}")


book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")

# Create borrowers
borrower1 = Borrower("1fwkwe")
borrower2 = Borrower("2sdfwko")

# Borrow books
borrower1.borrow_book(book1)  # Borrower 1 borrows book1
borrower2.borrow_book(book1)  # Try to borrow an already borrowed book

# Show book info
book1.show_info()
book2.show_info()

# Return books
borrower1.return_book(book1)
book1.show_info()

borrower2.borrow_book(book2)
borrower2.show_info()