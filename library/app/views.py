from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Avg, Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Author, Book

# Create your views here.


class BookListView(ListView):
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        q = self.request.GET.get("q")
        qs = Book.objects.prefetch_related("authors").annotate(
            avg_rating=Avg("reviews__rating")
        )

        if q:
            qs = Book.objects.filter(
                Q(name__icontains=q) | Q(authors__name__icontains=q)
            ).distinct()

        return qs


class BookDetailView(DetailView):
    model = Book

    def get_queryset(self):

        return Book.objects.prefetch_related(
            "authors", "genres", "reviews", "reviews__user", "reviews__user__user"
        ).annotate(avg_rating=Avg("reviews__rating"))


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book

    permission_required = "admin.change_book"

    fields = ["name", "description", "genres", "isbn", "authors", "image"]
    success_url = reverse_lazy("book-list")


class BookDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView,
):
    permission_required = "admin.delete_book"
    model = Book
    success_url = reverse_lazy("book-list")


class BookEditView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    permission_required = "admin.change_book"
    model = Book
    fields = ["name", "description", "genres", "isbn", "authors", "image"]
    success_url = reverse_lazy("book-list")


class AuthorDetailView(DetailView):
    model = Author
