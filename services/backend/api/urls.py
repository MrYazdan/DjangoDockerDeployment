from api.views import UserAPIView
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'user', UserAPIView, basename="users")

schema_view = get_schema_view(
    openapi.Info(
        title="Django server api",
        default_version='v1',
        description="Test api v1 description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^docs/redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", include(router.urls)),
]
