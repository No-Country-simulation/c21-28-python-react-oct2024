from rest_framework import viewsets
from .serializer import AddressesSerializer,CitiesSerializer
from .models import Addresses,Cities

# Create your views here.

class AddressesViewSet(viewsets.ModelViewSet):
    queryset=Addresses.objects.all()
    serializer_class=AddressesSerializer
    
class CitiesViewSet(viewsets.ModelViewSet):
    queryset=Cities.objects.all()
    serializer_class=CitiesSerializer