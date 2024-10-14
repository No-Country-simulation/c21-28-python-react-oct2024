from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

class CurrenciesViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer

class DepartamentsViewSet(viewsets.ModelViewSet):
    queryset = Departaments.objects.all()
    serializer_class = DepartamentsSerializer
    
class GendersViewSet(viewsets.ModelViewSet):
    queryset = Genders.objects.all()
    serializer_class = GendersSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemtypesViewSet(viewsets.ModelViewSet):
    queryset = Itemtypes.objects.all()
    serializer_class = ItemtypesSerializer

class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    
class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class PostalcodesViewSet(viewsets.ModelViewSet):
    queryset = Postalcodes.objects.all()
    serializer_class = PostalcodesSerializer

class ResourcesViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer

class StatesViewSet(viewsets.ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    
class SupplieritemsViewSet(viewsets.ModelViewSet):
    queryset = Supplieritems.objects.all()
    serializer_class = SupplieritemsSerializer

class SupplierplanitemsViewSet(viewsets.ModelViewSet):
    queryset = Supplierplanitems.objects.all()
    serializer_class = SupplierplanitemsSerializer

class SupplierplansViewSet(viewsets.ModelViewSet):
    queryset = Supplierplans.objects.all()
    serializer_class = SupplierplansSerializer

class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer