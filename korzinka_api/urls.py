from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register('', MahsulotlarViewset, basename='mahsulotlar')

urlpatterns = router.urls
