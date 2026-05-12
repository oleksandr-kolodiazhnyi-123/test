"""
API test cases.
"""

import pytest


@pytest.mark.django_db
def test_user_creation(user):
    """Test user fixture."""
    assert user.username == "testuser"


@pytest.mark.django_db
def test_authenticated_api(authenticated_client):
    """Test authenticated API client."""
    response = authenticated_client.get("/api/endpoint/")
    assert response.status_code == 200
