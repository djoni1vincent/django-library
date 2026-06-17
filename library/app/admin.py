from django.contrib import admin

from .models import Author, Book, Genre, Profile

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "isbn"]


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Profile)
