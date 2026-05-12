# Django Test Project

A production-ready Django 4.2 project following Python and Django best practices.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Development](#development)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Deployment](#deployment)
- [Best Practices](#best-practices)

## ✨ Features

- **Django 4.2 LTS** - Latest stable version
- **PostgreSQL** - Production-ready database
- **Django REST Framework** - Modern API development
- **Token Authentication** - Secure API endpoints
- **CORS Support** - Cross-origin requests handling
- **WhiteNoise** - Efficient static file serving
- **Comprehensive Logging** - File and console logging
- **Pytest** - Advanced testing framework
- **Code Quality Tools** - Black, Flake8, isort, Pylint
- **Security Headers** - HSTS, CSP, XSS protection
- **Docker Ready** - Containerization support

## 📁 Project Structure

```
test/
├── config/
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI application
├── tests/
│   ├── __init__.py
│   └── conftest.py      # Pytest fixtures
├── manage.py            # Django CLI
├── requirements.txt     # Dependencies
├── pyproject.toml       # Python project metadata
├── pytest.ini           # Pytest configuration
├── .flake8              # Flake8 linting
├── .gitignore           # Git ignore rules
├── .env.example         # Environment variables template
├── Makefile             # Development tasks
└── README.md            # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.10+
- PostgreSQL 12+
- pip and virtualenv

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/okolo123/test.git
   cd test
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your PostgreSQL credentials.

## 🏃 Quick Start

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Visit http://localhost:8000/admin
```

Or use the Makefile:

```bash
make migrate
make createsuperuser
make dev
```

## 🛠️ Development

### Available Commands

```bash
make install      # Install dependencies
make dev          # Run development server
make test         # Run tests with coverage
make lint         # Run code quality checks
make format       # Format code (Black, isort)
make migrate      # Run database migrations
make clean        # Clean cache and compiled files
```

### Creating a Django App

```bash
python manage.py startapp your_app_name
```

Add to `INSTALLED_APPS` in `config/settings.py`:
```python
INSTALLED_APPS = [
    ...
    "your_app_name",
]
```

### API Authentication

Token authentication is configured. Get a token:

```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_user", "password": "your_password"}'
```

Use the token:
```bash
curl -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/endpoint/
```

## 🧪 Testing

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov
```

View HTML coverage report:
```bash
pytest --cov --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

Example test fixture usage:

```python
def test_user_creation(user):
    """Test user fixture."""
    assert user.username == "testuser"

def test_authenticated_api(authenticated_client):
    """Test authenticated API client."""
    response = authenticated_client.get("/api/endpoint/")
    assert response.status_code == 200
```

## 🧹 Code Quality

### Format Code
```bash
# Black formatting
black .

# Import sorting
isort .

# Or both
make format
```

### Lint Code
```bash
# Run all checks
make lint

# Individual checks
black --check .
flake8 .
isort --check-only .
pylint your_module/
```

### Configuration

- **Black**: 88-character line length (PEP 8 compliant)
- **isort**: Black-compatible import sorting
- **Flake8**: Configured in `.flake8`
- **Pylint**: Configured in `pyproject.toml`

## 🔒 Security

### Production Settings

Before deploying, ensure:

1. **Change SECRET_KEY** in `.env`
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. **Set DEBUG=False** in `.env`

3. **Configure ALLOWED_HOSTS** in `.env`

4. **Use environment variables** for sensitive data

5. **Enable HTTPS** (automatic in production with DEBUG=False)

### Security Features

- ✅ HSTS (HTTP Strict Transport Security)
- ✅ CSP (Content Security Policy)
- ✅ XSS Protection
- ✅ CSRF Protection
- ✅ Secure Cookies (HTTPS only)
- ✅ CORS Configuration
- ✅ Token Authentication

## 🐳 Deployment

### Using Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Using Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t django-app .
docker run -p 8000:8000 django-app
```

### Environment Variables for Production

```bash
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=production_db
DB_USER=db_user
DB_PASSWORD=secure_password
DB_HOST=db.example.com
DB_PORT=5432
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

## 📚 Best Practices Implemented

### Django

- ✅ Environment-based configuration (12-factor app)
- ✅ PostgreSQL for production database
- ✅ DRF for REST API
- ✅ Token-based authentication
- ✅ Comprehensive logging
- ✅ Security middleware
- ✅ Static file handling with WhiteNoise

### Python

- ✅ PEP 8 compliant code
- ✅ Type hints support
- ✅ Comprehensive docstrings
- ✅ Proper exception handling
- ✅ Code formatting (Black)
- ✅ Import organization (isort)
- ✅ Linting (Flake8, Pylint)

### Development

- ✅ Pytest with fixtures
- ✅ Coverage reporting
- ✅ Makefile for common tasks
- ✅ Git ignore rules
- ✅ Environment templates
- ✅ Clear project structure

## 📖 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Black Code Formatter](https://github.com/psf/black)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Oleksandr K

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Happy coding!** 🎉
