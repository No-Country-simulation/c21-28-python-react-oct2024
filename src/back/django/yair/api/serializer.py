from rest_framework import serializers
from .models import Establishment, Company, Departament

class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'

