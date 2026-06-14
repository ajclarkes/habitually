# Habitually API

Django REST API for the Habitually app.

## Setup

Requires Python 3.12+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Running the server

```bash
python manage.py runserver
```

## Running tests

```bash
pytest
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/obs/health/` | Health check |
