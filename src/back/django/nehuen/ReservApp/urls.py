from django.urls import path, include
from rest_framework import routers
from ReservApp import views

router=routers.DefaultRouter()
router.register(r'Addresses',views.AddressesViewSet)
router.register(r'Cities',views.CitiesViewSet)

urlpatterns = [
    path('',include(router.urls))
]