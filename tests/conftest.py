"""
Pytest configuration and shared fixtures.
"""

import os

import django
import pytest
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.test import APIClient


def pytest_configure():
    """Configure Django settings for testing."""
    if not settings.configured:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
        django.setup()


@pytest.fixture
def user(db):
    """Create a test user."""
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="testpass123",
    )


@pytest.fixture
def admin_user(db):
    """Create a test admin user."""
    return User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="adminpass123",
    )


@pytest.fixture
def api_client():
    """Create an API client."""
    return APIClient()


@pytest.fixture
def authenticated_client(db, user):
    """Create an authenticated API client."""
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def admin_client(db, admin_user):
    """Create an authenticated admin API client."""
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client
