# E-commerce Skeleton

Base Django 5 project prepared for order-module coding challenge.

## Requirements

* Docker & Docker Compose
* (Alternative) Python 3.12+, PostgreSQL 16

## Quick start (recommended)

```bash
git clone <repo>
cp .env.example .env
docker compose up --build
```

Access docs at http://localhost:8000/api/docs/

## Manual start (without Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=postgres://ecommerce:ecommerce@localhost:5432/ecommerce
export DJANGO_SECRET_KEY=dev-secret-key
export DJANGO_DEBUG=1
python manage.py migrate
python manage.py runserver
```

## Tests

```bash
docker compose run --rm web pytest
```

Coverage reports will display in terminal (expected >= 80 %).

## Code style

The repository follows Black, isort and flake8 conventions. Format & lint:

```bash
black .
isort .
flake8
``` 