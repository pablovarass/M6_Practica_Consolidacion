from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
from .models import Vehiculo
from .forms import VehiculoForm


def crear_vehiculo(request):
    # Your logic for creating a vehicle
    return render(request, 'vehiculo/agregar.html')

def index(request):
    return render(request, 'index.html')

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    try:
        vehiculos = Vehiculo.objects.all()
        return render(request, 'listar.html', {'vehiculos': vehiculos})
    except PermissionDenied:
        messages.warning(request, 'No tienes permiso para ver el listado de vehículos.')
        return redirect('index')


def permission_denied_view(request, exception):
    messages.warning(request, 'No tienes permiso para acceder a esta página.')
    return redirect('index')


@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo agregado correctamente')  
            return redirect('listar_vehiculos')  
    else:
        form = VehiculoForm()
    return render(request, 'agregar.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Asigna el permiso 'visualizar_catalogo' al nuevo usuario
            content_type = ContentType.objects.get_for_model(Vehiculo)
            try:
                permission = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                print("El permiso 'visualizar_catalogo' no existe")
            
            # Autentica y loguea al usuario automáticamente
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registro exitoso y sesión iniciada')
                return redirect('index')
        else:
            print(form.errors)
            if 'username' in form.errors:
                messages.error(request, 'El nombre de usuario ya existe. Elige otro.')
            elif 'password2' in form.errors and any("didn't match" in str(error) for error in form.errors['password2']):
                messages.error(request, 'Los dos campos de contraseña no coinciden.')
            else:
                messages.error(request, 'Modifica los datos de ingreso.')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo modificado correctamente')
            return redirect('listar_vehiculos')
        else:
            messages.error(request, 'Modifica los datos de ingreso')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'editar_vehiculo.html', {'form': form, 'vehiculo_id': vehiculo_id})


@login_required    
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    vehiculo.delete()
    messages.info(request, 'Vehículo eliminado correctamente')
    return redirect('listar_vehiculos')


def iniciar_sesion(request):
    if not request.user.is_authenticated and request.GET.get('next'):
        # Add a message when redirected to login
        messages.info(request, 'Debes iniciar sesión para acceder a esta página.')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('index')  
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'login.html')
        
        
        
        
        
        
        
    
