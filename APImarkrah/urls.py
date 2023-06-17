from rest_framework import routers, permissions
from django.urls import path, include
from app import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Создаем объект Router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'tasks', views.tasksViewSet)

# Описание API для документации Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="My API description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# URL-адреса для работы с нашим API и документацией Swagger
urlpatterns = [
    # URL-адреса для нашего API
    path('', include(router.urls)),

    # URL-адреса документации Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
