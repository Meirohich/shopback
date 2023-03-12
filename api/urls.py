from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductApiView)
router.register(r'categories', views.CategoryApiView)

urlpatterns = [
    path('', include(router.urls)),
]
