# PRD – “E-commerce Skeleton” Base Project for Order Challenge

1. Purpose of the base project
Provide candidates with a fully working Django 5.0 repository, wired to PostgreSQL and Django Rest Framework, containing only one app called `products`. The `orders` module must be absent so the candidate can create it during the challenge.

2. Scope
•  Django project initialised with the standard structure.
•  PostgreSQL connection via `psycopg`.
•  DRF installed and configured with JSON renderer and browsable API.
•  `products` app with complete, documented REST endpoints.
•  Automatic API documentation via **drf-spectacular**.
•  `docker-compose.yml` script to spin up DB and local application.
•  Detailed **README** with setup, run and test instructions.

3. Out of scope
•  Any modelling or routes for orders.
•  Authentication and authorisation.
•  Payment processing, stock or shipping.

4. Personas
•  Developer Candidate: clones the repo, runs it locally and implements the orders module.
•  Interviewer: observes and evaluates reasoning and coding in real-time.

5. Relevant user stories
•  As a candidate, I want a project that runs within minutes so I can focus on order logic.
•  As a candidate, I want clear examples of model, serializer and viewset in the `products` app so I can follow the same pattern in `orders`.
•  As an interviewer, I want to access the product list via API to test order creation.

6. Functional requirements
6.1 Configuration
- Environment variables in `.env.example` for DB, debug and port.

6.2 `products` app
- `Product` model with fields: `id` (UUID PK), `name` (str, up to 120), `price` (decimal 10,2).
- Serializer detailing basic validations.
- ViewSet exposing list, retrieve, create, update, destroy.
- URLs registered under `/api/products/`.

6.3 Docs
- Route `/api/schema/` for OpenAPI schema.
- Route `/api/docs/` using Swagger UI.

7. Non-functional requirements
•  Minimum Python 3.12.
•  Code style: **Black**, **isort**, **flake8**.
•  Initial tests with **pytest** covering at least 80 % of `products`.
•  Docker build in under 2 minutes on modern hardware.
•  Project must start with `docker compose up --build` without manual intervention.

8. Architecture & folder structure
```
ecommerce/
  ecommerce/        # settings, urls, asgi, wsgi
  products/
    migrations/
    models.py
    serializers.py
    views.py
    urls.py
    tests/
  manage.py
docker-compose.yml
Dockerfile
requirements.txt
README.md
```

9. Initial data model
```
Product
  id           UUID        PK
  name         Char(120)
  price        Decimal(10,2)
  created_at   DateTime(auto_now_add)
  updated_at   DateTime(auto_now)
```

10. Existing endpoints
•  `GET    /api/products/` list products
•  `POST   /api/products/` create product
•  `GET    /api/products/{uuid}/` detail
•  `PUT    /api/products/{uuid}/` update
•  `DELETE /api/products/{uuid}/` remove
All return JSON as per serializer.

11. Environment configuration
•  Use **Poetry** or **pip-tools** to manage deps.
•  `DATABASE_URL` var in the form `postgres://user:pass@db:5432/ecommerce`.
•  `db` service in docker compose uses official `postgres:16-alpine` image.

12. Quick guide in README
```sh
git clone <repo>
cp .env.example .env
docker compose up --build
# open http://localhost:18000/api/docs/
```

13. Definition of Done for the base project
•  `docker compose up` starts the app and exposes `/api/docs/`.
•  Creating, listing and deleting a product via Swagger works.
•  `pytest` runs and returns minimum 80 % coverage.
•  No critical warnings from **flake8**. 