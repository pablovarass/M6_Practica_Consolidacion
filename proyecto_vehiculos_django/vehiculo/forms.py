from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese la marca del vehículo',
                'required': True
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el modelo del vehículo',
                'required': True
            }),
            'serial_carroceria': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el serial de la carrocería',
                'required': True
            }),
            'serial_motor': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el serial del motor',
                'required': True
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Seleccione la categoría del vehículo',
                'required': True
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el precio del vehículo',
                'required': True
            }),
        }
