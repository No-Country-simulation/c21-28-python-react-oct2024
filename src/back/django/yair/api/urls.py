from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'establishment', views.EstablishmentViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'departaments', views.DepartamentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]