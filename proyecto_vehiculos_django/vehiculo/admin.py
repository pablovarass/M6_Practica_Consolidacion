from django.contrib import admin
from .models import Vehiculo

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio')  # Campos que se mostrarán en la lista
    
admin.site.register(Vehiculo, VehiculoAdmin)
