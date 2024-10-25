from django.urls import path, include
from rest_framework import routers
from ReservApp import views

router=routers.DefaultRouter()
router.register(r'Addresses',views.AddressesViewSet)
router.register(r'Cities',views.CitiesViewSet)
router.register(r'Companies',views.CompaniesViewSet)
router.register(r'Contacts',views.ContactsViewSet)
router.register(r'Countries',views.CountriesViewSet)
router.register(r'Currencies',views.CurrenciesViewSet)
router.register(r'Departaments',views.DepartamentsViewSet)
router.register(r'Genders',views.GendersViewSet)
router.register(r'Items',views.ItemsViewSet)
router.register(r'Itemtypes',views.ItemtypesViewSet)
router.register(r'Locations',views.LocationsViewSet)
router.register(r'Notes',views.NotesViewSet)
router.register(r'Partners',views.PartnersViewSet)
router.register(r'Postalcodes',views.PostalcodesViewSet)
router.register(r'Resources',views.ResourcesViewSet)
router.register(r'States',views.StatesViewSet)
router.register(r'Supplieritems',views.SupplieritemsViewSet)
router.register(r'Supplierplanitems',views.SupplierplanitemsViewSet)
router.register(r'Supplierplans',views.SupplierplansViewSet)
router.register(r'Suppliers',views.SuppliersViewSet)

urlpatterns = [
    path('',views.mostrar_index,name='Home'),
    path('tablas/',include(router.urls)),
    path('registro/',views.registro_usuario,name='Registro'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_request, name='logout'),
    path('turno/',views.mostrar_turno, name='turno')
]