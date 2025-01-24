import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self, filename='library.json'):
        self.books = []
        self.filename = filename
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f'Book "{book.title}" added to the library.')

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nBooks in the library:")
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f'Found: {book}')
                return
        print(f'Book "{title}" not found in the library.')

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(**book) for book in books_data]
        except FileNotFoundError:
            print("No previous library data found. Starting fresh.")

def main():
    library = Library()

    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == '4':
            print("Exiting the library.")
            break
        elif choice == " ":
            continue
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
