from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from Admin.views import driver_panel, client_panel

schema_view = get_schema_view(
    openapi.Info(
        title="Driver Detection API",
        default_version="v1",
        description="Online driver detection and simple order assignment API documentation",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="youremail@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # Your app APIs
    path('api/v1/', include('Admin.urls'), name='api-v1'),
    path("driver/<int:driver_id>/", driver_panel, name="driver_panel"),
    path("client/", client_panel, name="client_panel"),

    # swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'
         ),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0
    ), name='schema-redoc')
]
