from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Book, Library

# Root path redirect to /books/
def home_redirect(request):
    return redirect('list_books')

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ full path

# Class-based view: Show library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ full path
    context_object_name = 'library'
