from re import search

from django.contrib import admin

from .models import Author, Book, Genre, Profile, Review

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "isbn"]
    search_fields = ["name", "authors__name", "isbn"]
    list_filter = ["genres"]


class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1 


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["book", "user", "rating"]


admin.site.register(Genre)
admin.site.register(Profile)
