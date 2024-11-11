# Generated by Django 4.0.5 on 2024-11-11 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0006_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar Catálogo de Vehículos'), ('vehiculo.view', 'Puede ver los vehículos'), ('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')], 'verbose_name': 'Vehículo', 'verbose_name_plural': 'Vehículos'},
        ),
    ]
