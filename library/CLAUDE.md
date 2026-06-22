# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

This is a **learning project** — the user is following a structured Junior → Middle Django roadmap.

Full roadmap: `/Users/djoni1vincent/djoni/Obsidian-notes/100 Programming/Django Roadmap 2026.md`

**Current phase: Фаза 1 — Django Hardening (Library / Book Club)**

| Topic | Status |
|---|---|
| Custom User Model (AbstractUser + bio/avatar) | ✅ done |
| ORM N+1 / `select_related` / `prefetch_related` | ✅ done |
| Class-Based Views (CRUD + Mixins) | ✅ done |
| Advanced ORM (`Q`, `annotate`, `aggregate`) | ✅ done |
| PostgreSQL (migrated from SQLite) | ✅ done |
| Testing with `pytest-django` + Factory Boy | ✅ done |
| Django Signals (`post_save`, `pre_delete`) | ✅ done |
| Middleware (custom request logger) | ✅ done |
| Admin customization (`list_display`, filters, actions, inlines) | ✅ done |

**After Phase 1:** Phase 2 — DRF + API (new project: E-commerce Product API).

### How to assist

- When explaining concepts, assume Python is solid but Django details may be new.
- Don't re-explain already-completed topics (see table above) unless asked.
- When writing code for this project, prefer patterns that teach — e.g. show the `select_related` call rather than hiding it in a manager.
- Suggest improvements only if they relate to what the user is currently learning in Phase 1.

---

## Commands

All commands run from `library/` (the Django project root containing `manage.py`).

```bash
# Run dev server
python manage.py runserver

# Run all tests
pytest

# Run a single test function
pytest app/tests.py::test_can_create_book

# Run tests with coverage
pytest --cov=app

# Apply migrations
python manage.py migrate

# Create new migration after model changes
python manage.py makemigrations
```

Dependencies are managed with `uv` (`pyproject.toml` / `uv.lock`). The virtualenv is at `.venv/`.

## Environment

The project uses `python-decouple` to read DB credentials from a `.env` file (or environment variables). Required keys: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`. The database is **PostgreSQL** — SQLite config is commented out in `settings.py`.

## Architecture

Single Django app (`app/`) inside the `library` project package.

**Models** (`app/models.py`):
- `Book` — core entity; M2M to `Author` and `Genre`; has `ISBNField` and an image upload; ordered by name.
- `Author`, `Genre` — supporting lookup tables.
- `Review` — FK to `Book` and `Profile`; holds a rating (int) and text description.
- `Profile` — extends `User` via OneToOne; holds bio and avatar image.

**Signals** (`app/signals.py`): `post_save` on `User` auto-creates/saves the linked `Profile`. `pre_delete` on `Profile` removes the avatar file from disk (skips the default avatar).

**Views** (`app/views.py`): all class-based views. `BookListView` supports `?q=` search across book name and author name and annotates with `avg_rating`. `BookDetailView` prefetches all review/author/genre relations. Create/Edit/Delete views require login + explicit `admin.*_book` permissions.

**URL layout**: app routes are mounted at `/` (root). Auth URLs at `/accounts/` (Django's built-in). `django-debug-toolbar` URLs are appended automatically. Media files are served by Django in `DEBUG` mode.

**Templates**: global base at `templates/main.html`; auth templates under `templates/registration/`. App templates follow Django's default `<app>/book_list.html`, `<app>/book_detail.html` convention.

**Testing**: pytest with `pytest-django`. Tests live in `app/tests.py`. `pytest.ini` sets `DJANGO_SETTINGS_MODULE = library.settings` (uses the real PostgreSQL DB — no separate test settings). `factory-boy` is available for fixtures.

**Permissions**: Book create/edit/delete is gated on `admin.change_book` / `admin.delete_book` Django permissions, not a custom permission class — grant these through the admin site or Django shell.
