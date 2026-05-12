"""
URL routing configuration for Django project.
"""

from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_endpoint(request):
    """A simple authenticated API endpoint."""
    return Response({"message": "Hello, world!"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    path("api/endpoint/", api_endpoint, name="api_endpoint"),
]
