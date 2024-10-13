from rest_framework import serializers 
from .models import Addresses,Cities

class AddressesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Addresses
        fields= '__all__'

class CitiesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cities
        fields= '__all__'