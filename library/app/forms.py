from django import forms

from .models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "authors": forms.CheckboxSelectMultiple,
            "genres": forms.CheckboxSelectMultiple,
        }
