from django.urls import path
from . import views
from . views import registro, eliminar_vehiculo, login, iniciar_sesion

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/list/', views.listar_vehiculos, name='listar_vehiculos'),
    path('registro/', registro, name='registro'),
    path('vehiculo/edit/<int:vehiculo_id>/', views.editar_vehiculo, name='editar_vehiculo'),  
    path('delete/<int:vehiculo_id>/', eliminar_vehiculo, name='eliminar_vehiculo'),  
    path('login/', iniciar_sesion, name='login'), # registrando ruta para el login
]

