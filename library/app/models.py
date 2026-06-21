from django.contrib.auth.models import User
from django.db import models
from isbn_field import ISBNField

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to="avatars/", default="avatar-default.jpg", blank=True
    )

    def __str__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(
        max_length=100, help_text="Enter title of the book", unique=True
    )
    description = models.TextField(
        help_text="Enter description of the book", blank=True
    )
    genres = models.ManyToManyField(Genre, related_name="books", blank=True)
    isbn = ISBNField(
        help_text="Enter the 10 or 13 digit International Standard Book Number",
        blank=True,
    )
    authors = models.ManyToManyField(Author, related_name="books", blank=True)
    image = models.ImageField(upload_to="book_images/", default="book_default.jpg")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="reviews", blank=True, null=True, on_delete=models.CASCADE
    )
    description = models.TextField(
        blank=True, help_text="Write here your review on the book."
    )

    def __str__(self):
        return str(self.book)
