# from django.urls import reverse_lazy
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from .models import Author, Book

# Create your views here.


class BookListView(ListView):
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        q = self.request.GET.get("q")
        qs = Book.objects.all()

        if q:
            qs = Book.objects.filter(Q(name__icontains=q) | Q(authors__name__icontains=q)).distinct()

        return qs


class BookDetailView(DetailView):
    model = Book


class AuthorCreateView(CreateView):
    model = Author
    fields = ["name", "description"]
    template_name = "app/author_create_form.html"
    success_url = reverse_lazy("book-list")


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "app/author_delete_form.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "app/author_detail.html"
