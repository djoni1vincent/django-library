# Create your tests here.
import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from app.models import Author, Book, Genre, Profile, Review


@pytest.mark.django_db
def test_can_create_book():
    book = Book.objects.create(
        name="Дюна",
        description="Роман про пустынную планету",
    )
    assert book.name == "Дюна"
    assert str(book) == "Дюна"


@pytest.mark.django_db
def test_can_create_author():
    author = Author.objects.create(
        name="Иванов",
        description="Государь",
    )
    assert author.name == "Иванов"
    assert str(author) == "Иванов"


@pytest.mark.django_db
def test_can_create_genre():
    genre = Genre.objects.create(
        name="Фантастика",
    )
    assert genre.name == "Фантастика"
    assert str(genre) == "Фантастика"


@pytest.mark.django_db
def test_can_create_profile():
    user = User.objects.create(
        username="testuser",
        password="testpassword",
    )
    assert Profile.objects.filter(user=user).exists()
    assert str(user.profile) == "testuser"


@pytest.mark.django_db
def test_can_create_review():
    user = User.objects.create(
        username="testuser",
        password="testpassword",
    )

    book = Book.objects.create(
        name="Дюна",
        description="Роман про пустынную планету",
    )

    review = Review.objects.create(
        book=book,
        user=user.profile,
        description="Отличная книга!",
    )
    assert review.description == "Отличная книга!"
    assert review.book == book
    assert str(review.description) == "Отличная книга!"


@pytest.mark.django_db
def test_book_list_view_returns_200(client):
    response = client.get(reverse("book-list"))  # имя url-паттерна из твоих urls.py
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_detail_view_returns_200(client):
    book = Book.objects.create(
        name="Дюна",
        description="Роман про пустынную планету",
    )
    response = client.get(reverse("book-detail", kwargs={"pk": book.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_create_view_redirects_anonymous_user(client):
    response = client.get(reverse("book-create"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_book_create_view_forbidden_for_regular_user(client):
    user = User.objects.create_user(username="regularuser", password="testpass123")
    client.force_login(user)
    response = client.get(reverse("book-create"))
    assert response.status_code == 403


@pytest.mark.django_db
def test_search_in_book_list(client):
    book = Book.objects.create(
        name="Дюна",
        description="Роман про пустынную планету",
    )
    response = client.get(reverse("book-list"), {"q": "Дюна"})
    assert response.status_code == 200
    assert book in response.context["object_list"]
