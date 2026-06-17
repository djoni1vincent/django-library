from django.urls import path

from .views import BookView, DetailBookView

urlpatterns = [
    path("", BookView.as_view(), name="book-list"),
    path("book/<int:pk>/", DetailBookView.as_view(), name="book-detail"),
]
