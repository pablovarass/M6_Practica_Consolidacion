from django.contrib import admin
from .models import Vehiculo
from django import forms


admin.site.register(Vehiculo)

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
