from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Departamento, Habilidad, Empleado
admin.site.register(Departamento)
admin.site.register(Habilidad)
admin.site.register(Empleado)

