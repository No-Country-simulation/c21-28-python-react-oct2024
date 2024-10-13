from rest_framework import viewsets
from .serializer import EstablishmentSerializer, CompanySerializer, DepartamentSerializer
from .models import Establishment, Company, Departament

# Create your views here.

class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer