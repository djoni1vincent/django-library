from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import Book
from .forms import BookCreateForm

# Create your views here.


class BookListView(ListView):
    model = Book
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = "app/book_create_form.html"
    success_url = reverse_lazy("book-list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
