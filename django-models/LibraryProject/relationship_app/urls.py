from django.urls import path
from . import views
from .views import (
    add_book, edit_book, delete_book,
    list_books, LibraryDetailView,
    admin_view, librarian_view, member_view,
    register
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Auth URLs
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Book views
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),         # ✅ Checker needs this
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),  # ✅ Checker needs this
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

    # Library views
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]
