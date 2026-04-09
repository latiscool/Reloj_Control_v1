from django.contrib.auth.models import AbstractUser
from django.db import models

class Empleado(AbstractUser):
    """
    Modelo de usuario personalizado para el sistema Reloj Control.
    
    Hereda de AbstractUser para conservar la seguridad nativa de Django 
    (hashing de contraseñas, manejo de sesiones, first_name, last_name, email).
    Se extiende para cumplir con los requerimientos institucionales añadiendo
    identificadores nacionales y estructura organizacional.
    """
    
    # Identificador nacional único. Se exige nivel de base de datos (unique=True)
    # para evitar registros de asistencia duplicados o suplantación.
    rut = models.CharField(
        max_length=12, 
        unique=True, 
        help_text="Formato: 12.345.678-9"
    )
    
    # Datos organizacionales. 
    # blank=True permite que los formularios de Django no exijan este campo.
    # null=True permite que PostgreSQL guarde el valor como NULL si no hay datos.
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # Configuración visual para el panel de administración de Django
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """
        Representación en cadena del objeto Empleado.
        Utilizado en el panel de administración y logs de depuración.
        """
        # get_full_name() es un método nativo heredado que concatena de forma
        # segura los campos first_name y last_name, manejando espacios vacíos.
        return f"{self.rut} - {self.get_full_name()}"