from django.urls import path

from .views import (
    AuthorCreateView,
    AuthorDeleteView,
    AuthorDetailView,
    BookDetailView,
    BookListView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("author/create/", AuthorCreateView.as_view(), name="author-create"),
    path("author/delete/<int:pk>", AuthorDeleteView.as_view(), name="author-delete"),

]
