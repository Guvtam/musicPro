from django.urls import path, include
from rest_framework import routers
from .api import  UserViewSet, UserRegistrationViewSet


router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

