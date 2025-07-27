import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No author named {author_name} found.")

# Query 2: All books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name} Library:")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")

# Query 3: Get the librarian of a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # ✅ line added here
        print(f"Librarian of {library_name} Library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

# Sample Execution
if __name__ == "__main__":
    books_by_author("Chinua Achebe")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
