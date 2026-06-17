from isbn_field import ISBNField
from django.db import models
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    pass


class Book(models.Model):
    name = models.CharField(max_length=100, help_text="Enter title of the book")
    description = models.TextField(help_text="Enter description of the book")
    genres = models.ManyToManyField(Genre, related_name="books")
    isbn = ISBNField(help_text="Enter the 10 or 13 digit International Standard Book Number")
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.name
