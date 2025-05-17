from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

# This code defines the URL patterns for the book management application. It includes paths for listing books, viewing book details, adding a new book, editing an existing book, and deleting a book. Each path is associated with a specific view function that handles the request and response for that URL.