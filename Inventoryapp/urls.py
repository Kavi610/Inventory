from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Viewsets import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]