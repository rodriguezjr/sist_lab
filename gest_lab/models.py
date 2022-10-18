from django.db import models

# Create your models here.
class cliente(models.Model):
    """tabla de cliente de la bdd"""
    cedula = models.IntegerField(null=True, unique=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    f_nac = models.DateField()
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    id_grupo_sanguineo = models.ForeignKey('examen', on_delete=models.CASCADE, null=True, blank=True)
    id_sexo = models.ForeignKey('sexo', on_delete=models.PROTECT)
    def __str__(self):
        return '%s - %s %s' % (str(self.cedula), str(self.nombre), str(self.apellido))

class personal(models.Model):
    """tabla de personal de la bdd"""
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    id_sexo = models.ForeignKey('sexo', on_delete=models.PROTECT)
    id_cargo = models.ForeignKey('cargo', on_delete=models.CASCADE)

class cargo(models.Model):
    """docstring for cargo"""
    cargo = models.CharField(max_length=15)

    def __str__(self):
        return self.cargo

class sexo(models.Model):
    """docstring for sexo"""
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.sexo

class analisis(models.Model):
    """docstring for analisis"""
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class rango(models.Model):
    edad = models.IntegerField()
    lim_sup = models.FloatField()
    lim_inf = models.FloatField()
    id_insumo = models.ForeignKey('insumo', on_delete=models.CASCADE)
    id_sexo = models.ForeignKey('sexo', on_delete=models.PROTECT, null=True)
    
class insumo(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField()
    uso = models.FloatField()
    dosificacion = models.FloatField()
    id_unidad = models.ForeignKey('unidad', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class unidad(models.Model):
    unidad = models.CharField(max_length=10)
    
    def __str__(self):
        return self.unidad

class examen(models.Model):
    n_orden = models.CharField(max_length=15)
    id_cliente = models.ForeignKey('cliente', on_delete=models.PROTECT)
    f_solicitud = models.DateTimeField()
    f_proceso = models.DateTimeField(null=True, blank=True)
    f_validado = models.DateTimeField(null=True, blank=True)
    f_entrega = models.DateTimeField(null=True, blank=True)
    solicitud_id_personal = models.ForeignKey('personal', related_name='solicitado_por', on_delete=models.PROTECT)
    proceso_id_personal = models.ForeignKey('personal',  related_name='procesado_por', on_delete=models.PROTECT, null=True, blank=True)
    validado_id_personal = models.ForeignKey('personal', related_name='validado_por', on_delete=models.PROTECT, null=True, blank=True)
    entrega_id_personal = models.ForeignKey('personal', related_name='entragado_por', on_delete=models.PROTECT, null=True, blank=True)
    id_prueba = models.ForeignKey('prueba', on_delete=models.PROTECT)
    id_analisis = models.ForeignKey('analisis', on_delete=models.PROTECT)
    def __str__(self):
        return '%s %s %s' % (str(self.n_orden) ,str(self.id_prueba), str(self.id_cliente))

class prueba(models.Model):
    nombre = models.CharField(max_length=50)
    grupo = models.BooleanField()
    id_categoria = models.ForeignKey('categoria', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class opcion(models.Model):
    resultado = models.CharField(max_length=15)

    def __str__(self):
        return self.resultado

class categoria(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class subcategoria(models.Model):
    nombre = models.CharField(max_length=15)
    id_prueba = models.ForeignKey('prueba', on_delete=models.PROTECT)

class cuantitativa(models.Model):
    id_prueba = models.ForeignKey('prueba', on_delete=models.CASCADE)
    id_unidad = models.ForeignKey('unidad', on_delete=models.PROTECT)
    def __str__(self):
        return '%s se mide en %s' % (str(self.id_prueba), str(self.id_unidad)) 

class cualitativa(models.Model):
    id_prueba = models.ForeignKey('prueba', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_prueba) 

class descriptiva(models.Model):
    id_prueba = models.ForeignKey('prueba', on_delete=models.CASCADE) 

class cualitativa_opcion(models.Model):
    id_cualitativa = models.ForeignKey('cualitativa', on_delete=models.CASCADE)
    id_opcion = models.ForeignKey('opcion', on_delete=models.CASCADE)
    def __str__(self):
        return ('%s ---> %s' % (str(self.id_cualitativa),  str(self.id_opcion))) 

class resultado_cualitativo(models.Model):
    id_examen = models.ForeignKey('examen', on_delete=models.CASCADE)
    id_cualitativa_opcion = models.ForeignKey('cualitativa_opcion', on_delete=models.CASCADE)
    def __str__(self):
        return ('%s ---> %s' % (str(self.id_examen),  str(self.id_cualitativa_opcion))) 

class resultado_cuantitativo(models.Model):
    id_examen = models.ForeignKey('examen', on_delete=models.CASCADE)
    valor = models.FloatField()

class resultado_descriptivo(models.Model):
    id_examen = models.ForeignKey('examen', on_delete=models.CASCADE)
    resultado = models.TextField()

class analisis_prueba(models.Model):
    id_analisis = models.ForeignKey('analisis', on_delete=models.CASCADE)
    id_prueba = models.ForeignKey('prueba', on_delete=models.CASCADE)
    def __str__(self):
        return ('%s ---> %s' % (str(self.id_analisis),  str(self.id_prueba))) 

class insumo_prueba(models.Model):
    id_insumo = models.ForeignKey('insumo', on_delete=models.CASCADE)
    id_prueba = models.ForeignKey('prueba', on_delete=models.CASCADE)
    def __str__(self):
        return ('%s ---> %s' % (str(self.id_insumo),  str(self.id_prueba))) 