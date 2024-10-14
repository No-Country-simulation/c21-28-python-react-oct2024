from rest_framework import serializers
from .models import *


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = "__all__"


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = "__all__"

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = "__all__"

class DepartamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departaments
        fields = "__all__"

class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genders
        fields = "__all__"

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"

class ItemtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemtypes
        fields = "__all__"

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = "__all__"

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = "__all__"
    
class PostalcodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postalcodes
        fields = "__all__"

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = "__all__"

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = "__all__"

class SupplieritemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplieritems
        fields = "__all__"

class SupplierplanitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplierplanitems
        fields = "__all__"

class SupplierplansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplierplans
        fields = "__all__"

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = "__all__"