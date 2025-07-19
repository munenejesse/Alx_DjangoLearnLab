from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in list view
    list_filter = ('author', 'publication_year')            # Sidebar filters
    search_fields = ('title', 'author')                     # Search box fields
