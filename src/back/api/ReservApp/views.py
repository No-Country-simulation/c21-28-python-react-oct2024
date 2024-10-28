from rest_framework import viewsets
from .serializer import *
from ReservApp.models import *
from django.shortcuts import get_object_or_404, redirect, render
from .forms import  UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
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
    
    
def mostrar_index(request):
    
    return render(request,'ReservApp/index.html')    
    
def registro_usuario(request):
    if request.method =="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso!Bienvenido/a')
            return render(request,'ReservApp/index.html')
    else:
        form=UserRegisterForm()
        
    return render(request,'ReservApp/registro.html', {'form':form})
    
@csrf_protect
def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contra= form.cleaned_data.get('password')
            
            user= authenticate(username=usuario, password=contra)
            
            
            if user is not None:
                login(request,user)
                
                return render(request,'ReservApp/turno.html',{"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request,"ResevApp/login.html",{"mensaje":"Error,datos incorrectos"})
            
        else:
            return render(request,"ResevApp/login.html",{"mensaje":"Error,formulario erroneo"})
        
    form = AuthenticationForm()
    
    return render(request,"ReservApp/login.html",{'form':form})
# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             usuario = form.cleaned_data.get('username')
#             contra = form.cleaned_data.get('password')

#             user = authenticate(username=usuario, password=contra)

#             if user is not None:
#                 login(request, user)
#                 #return redirect(request,'index.html', {"mensaje": f"Bienvenido {usuario}"})
#                 return render(request, 'ReservApp/index.html', {"mensaje": f"Bienvenido {usuario}"})
#             else:
#                 return render(request, "ReservApp/login.html", {"form": form, "mensaje": "Error: usuario o contraseña incorrectos."})

#         else:
#             return render(request, "ReservApp/login.html", {"form": form, "mensaje": "Error: formulario erróneo."})

#     form = AuthenticationForm()
#     return render(request, "ReservApp/login.html", {'form': form})


def logout_request(request):
    logout(request)
    return render(request,"ReservApp/index.html",{"mensaje":"Has cerrado sesion exitosamente"})

    
def mostrar_turno(request):
    
    return render(request,'ReservApp/turno.html')   