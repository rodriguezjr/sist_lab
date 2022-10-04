from django.contrib import admin

from gest_lab.models import cliente
from gest_lab.models import personal
from gest_lab.models import cargo
from gest_lab.models import sexo
from gest_lab.models import analisis
from gest_lab.models import rango
from gest_lab.models import insumo
from gest_lab.models import unidad
from gest_lab.models import examen
from gest_lab.models import prueba
from gest_lab.models import opcion
from gest_lab.models import categoria
from gest_lab.models import subcategoria
from gest_lab.models import cuantitativa
from gest_lab.models import cualitativa
from gest_lab.models import descriptiva
from gest_lab.models import cualitativa_opcion
from gest_lab.models import resultado_cualitativo
from gest_lab.models import resultado_cuantitativo
from gest_lab.models import resultado_descriptivo
from gest_lab.models import analisis_prueba
from gest_lab.models import insumo_prueba
# Register your models here.

class clienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','telefono')

class analisis_pruebaAdmin(admin.ModelAdmin):
    list_display=('id_analisis','id_prueba')

class pruebaAdmin(admin.ModelAdmin):
    list_display=('nombre','id_categoria')

class cuantitativaAdmin(admin.ModelAdmin):
    list_display=('id_prueba','id_unidad')

class cualitativa_opcionAdmin(admin.ModelAdmin):
    list_display=('id_cualitativa','id_opcion')

class resultado_cualitativoAdmin(admin.ModelAdmin):
	list_display=('id_examen', 'id_cualitativa_opcion')

class resultado_cuantitativoAdmin(admin.ModelAdmin):
	list_display=('id_examen', 'valor')

admin.site.register(cliente, clienteAdmin)
admin.site.register(personal)
admin.site.register(cargo)
admin.site.register(sexo)
admin.site.register(analisis)
admin.site.register(rango)
admin.site.register(insumo)
admin.site.register(unidad)
admin.site.register(examen)
admin.site.register(prueba, pruebaAdmin)
admin.site.register(opcion)
admin.site.register(categoria)
admin.site.register(subcategoria)
admin.site.register(cuantitativa, cuantitativaAdmin)
admin.site.register(cualitativa)
admin.site.register(descriptiva)
admin.site.register(cualitativa_opcion, cualitativa_opcionAdmin)
admin.site.register(resultado_cualitativo, resultado_cualitativoAdmin)
admin.site.register(resultado_cuantitativo, resultado_cuantitativoAdmin)
admin.site.register(resultado_descriptivo)
admin.site.register(analisis_prueba, analisis_pruebaAdmin)
admin.site.register(insumo_prueba)