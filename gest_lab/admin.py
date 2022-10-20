from django.contrib import admin

from gest_lab.models import Cliente
from gest_lab.models import Usuario
from gest_lab.models import Cargo
from gest_lab.models import Sexo
from gest_lab.models import Examen
from gest_lab.models import Rango
from gest_lab.models import Insumo
from gest_lab.models import PruebaInsumo
from gest_lab.models import Unidad
from gest_lab.models import Solicitud
from gest_lab.models import Prueba
from gest_lab.models import Opcion
from gest_lab.models import Categoria
from gest_lab.models import Subcategoria
from gest_lab.models import Cuantitativa
from gest_lab.models import Cualitativa
from gest_lab.models import Descriptiva
from gest_lab.models import CualitativaOpcion
from gest_lab.models import ResultadoCualitativo
from gest_lab.models import ResultadoCuantitativo
from gest_lab.models import ResultadoDescriptivo
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','telefono')

class PruebaInsumoAdmin(admin.ModelAdmin):
    list_display=('prueba','insumos')

class PruebaAdmin(admin.ModelAdmin):
    list_display=('nombre','categoria')

class CuantitativaAdmin(admin.ModelAdmin):
    list_display=('prueba','unidad')

class ResultadoCualitativoAdmin(admin.ModelAdmin):
    list_display=('solicitud', 'cualitativa_opcion')

class ResultadoCuantitativoAdmin(admin.ModelAdmin):
    list_display=('solicitud', 'valor')

class CualitativaOpcionAdmin(admin.ModelAdmin):
    list_display=('cualitativa', 'opcion')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Usuario)
admin.site.register(Cargo)
admin.site.register(Sexo)
admin.site.register(Examen)
admin.site.register(Rango)
admin.site.register(Insumo)
admin.site.register(Unidad)
admin.site.register(Solicitud)
admin.site.register(Prueba, PruebaAdmin)
admin.site.register(Opcion)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Cuantitativa, CuantitativaAdmin)
admin.site.register(Cualitativa)
admin.site.register(Descriptiva)
admin.site.register(ResultadoCualitativo, ResultadoCualitativoAdmin)
admin.site.register(ResultadoCuantitativo, ResultadoCuantitativoAdmin)
admin.site.register(ResultadoDescriptivo)
admin.site.register(PruebaInsumo, PruebaInsumoAdmin)
admin.site.register(CualitativaOpcion, CualitativaOpcionAdmin)

