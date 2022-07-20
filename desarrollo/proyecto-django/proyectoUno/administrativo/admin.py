from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Propietario, Departamento

# Estudiante
class PropietarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')

admin.site.register(Propietario, PropietarioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
     
    list_display = ('costo_depa', 'num_cuartos', 'propietario')
    
    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
