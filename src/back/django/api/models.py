from django.db import models

# Create your models here.

class Establishment(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    denomination = models.CharField(max_length=100)
    is_active = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Companies'

class Departament(models.Model):
    departament_id = models.AutoField(primary_key=True)
    city_id = models.IntegerField()  # Debes definir el modelo City si es necesario
    description = models.CharField(max_length=100)
    is_active = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='departaments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Departaments'