from django.db import models

class Vehiculo(models.Model):
    MARCA_CHOICES = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    
    CATEGORIA_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    
    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def condicion_precio(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif 10000 < self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'
            
    def __str__(self):
        return f"{self.marca} {self.modelo}"

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        permissions = [
            # ('permiso', 'descripcion')
            ('visualizar_catalogo', 'Puede visualizar Catálogo de Vehículos'),
            ('vehiculo.view', 'Puede ver los vehículos'),
            # ('add_vehiculomodel', 'Puede agregar modelo de vehículo'), Usaremos el permiso automático de Dajano vehiculo.add_vehiculo
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como Scrum Master'),
            ('product_owner', 'Permiso como Product Owner')
        ]


        
