from django.urls import include, path
from rest_framework import routers
from .api import ProductoViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
