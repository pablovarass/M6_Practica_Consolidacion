from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo

@receiver(post_save, sender=User)
def asignar_permiso_catalogo(sender, instance, created, **kwargs):
    if created:
        # Obtener o crear el permiso
        content_type = ContentType.objects.get_for_model(Vehiculo)
        permission, created = Permission.objects.get_or_create(
            codename='visualizar_catalogo',
            name='Puede visualizar catálogo',
            content_type=content_type,
        )
        # Asignar el permiso al usuario
        instance.user_permissions.add(permission)
