from django.shortcuts import render

from django.views.generic import ListView
from .models import Book


# Create your views here.


def BookView(ListView):
    model = Book

    books = model
    context = {
        "books": books
    }

    return render("app/index.html", context)
