from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.


class BookView(ListView):
    model = Book
    context_object_name = "books"

class DetailBookView(DetailView):
    model = Book

