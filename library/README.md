# Library — Book Catalog

A Django web application for browsing and managing a book catalog with authors, genres, and reader reviews.

## Features

- Book catalog with search by title and author
- Average rating from reader reviews
- Book detail pages with authors, genres, and reviews
- CRUD for books (staff only)
- User authentication with profile (bio + avatar)
- Custom request logger middleware
- Django Admin with search, filters, and inline editing

## Tech Stack

- Python 3.14 / Django 6
- PostgreSQL
- pytest + pytest-django
- django-debug-toolbar

## Setup

**1. Clone and install dependencies**
```bash
git clone https://github.com/<your-username>/django-library.git
cd django-library/library
uv sync
```

**2. Configure environment**
```bash
cp .env.example .env
# fill in your PostgreSQL credentials
```

**3. Run migrations and start**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Running Tests

```bash
pytest
pytest --cov=app  # with coverage
```

## Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Description |
|---|---|
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL user |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port |
