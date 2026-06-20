from django.urls import path

from .views import (
    AuthorDetailView,
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookEditView,
    BookListView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("book/create/", BookCreateView.as_view(), name="book-create"),
    path("author/delete/<int:pk>", BookDeleteView.as_view(), name="book-delete"),
    path("author/edit/<int:pk>", BookEditView.as_view(), name="book-edit"),
]
