from django.db import models

# Create your models here.
class Cliente(models.Model):
    """tabla de cliente de la bdd"""
    cedula = models.IntegerField(null=True, unique=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    f_nac = models.DateField()
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    grupo_sanguineo = models.CharField(max_length=4)
    sexo = models.ForeignKey('Sexo', on_delete=models.PROTECT)
    
    def __str__(self):
        return '%s - %s %s' % (str(self.cedula), str(self.nombre), str(self.apellido))


class Usuario(models.Model):
    """tabla de usuario de la bdd"""
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    sexo = models.ForeignKey('Sexo', on_delete=models.PROTECT)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s - %s' % (str(self.nombre), str(self.cargo))


class Cargo(models.Model):
    """docstring for cargo"""
    cargo = models.CharField(max_length=15)

    def __str__(self):
        return self.cargo


class Sexo(models.Model):
    """docstring for sexo"""
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.sexo


class Examen(models.Model):
    """docstring for examen"""
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre
    
    class Meta():
        verbose_name_plural = 'Examenes'
            

class Rango(models.Model):
    edad = models.IntegerField()
    lim_sup = models.FloatField()
    lim_inf = models.FloatField()
    insumo = models.ForeignKey('Insumo', on_delete=models.CASCADE)
    sexo = models.ForeignKey('Sexo', on_delete=models.PROTECT, null=True)


class Unidad(models.Model):
    unidad = models.CharField(max_length=10)
    
    def __str__(self):
        return self.unidad

    class Meta():
        verbose_name_plural = 'Unidades'


class Solicitud(models.Model):
    n_orden = models.CharField(max_length=15)
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT)
    f_solicitud = models.DateTimeField(auto_now_add=True)
    f_proceso = models.DateTimeField(null=True, blank=True)
    f_validado = models.DateTimeField(null=True, blank=True)
    f_entrega = models.DateTimeField(null=True, blank=True)
    solicitud_usuario = models.ForeignKey('Usuario', related_name='solicitado_por', on_delete=models.PROTECT)
    proceso_usuario = models.ForeignKey('Usuario',  related_name='procesado_por', on_delete=models.PROTECT, null=True, blank=True)
    validado_usuario = models.ForeignKey('Usuario', related_name='validado_por', on_delete=models.PROTECT, null=True, blank=True)
    entrega_usuario = models.ForeignKey('Usuario', related_name='entragado_por', on_delete=models.PROTECT, null=True, blank=True)
    prueba = models.ForeignKey('Prueba', on_delete=models.PROTECT)
    examen = models.ForeignKey('Examen', on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s %s' % (str(self.n_orden) ,str(self.prueba), str(self.cliente))
    
    class Meta():
        verbose_name_plural = 'Solicitudes'


class Prueba(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    examen = models.ForeignKey('Examen', on_delete=models.PROTECT, null=True, blank=True)
    insumos = models.ManyToManyField('Insumo', through='PruebaInsumo')

    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=50)
    limite_alerta = models.FloatField()
    unidades = models.FloatField()
    unidad = models.ForeignKey('Unidad', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class PruebaInsumo(models.Model):
    prueba = models.ForeignKey('Prueba', on_delete=models.CASCADE)
    insumos = models.ForeignKey('Insumo', on_delete=models.CASCADE)
    cantidad = models.FloatField()

    class Meta():
        verbose_name_plural = 'PruebaInsumos'
        db_table = 'gest_lab_prueba_insumo'

class Categoria(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=15)
    prueba = models.ForeignKey('Prueba', on_delete=models.PROTECT)


class Cuantitativa(models.Model):
    prueba = models.ForeignKey('Prueba', on_delete=models.CASCADE)
    unidad = models.ForeignKey('Unidad', on_delete=models.PROTECT)
    def __str__(self):
        return '%s se mide en %s' % (str(self.prueba), str(self.unidad)) 


class Descriptiva(models.Model):
    prueba = models.ForeignKey('Prueba', on_delete=models.CASCADE)


class Cualitativa(models.Model):
    prueba = models.ForeignKey('Prueba', on_delete=models.CASCADE)
    opciones = models.ManyToManyField('Opcion', through='CualitativaOpcion')
    def __str__(self):
        return str(self.prueba)


class Opcion(models.Model):
    resultado = models.CharField(max_length=15)

    def __str__(self):
        return self.resultado

    class Meta():
        verbose_name_plural = 'Opciones'


class CualitativaOpcion(models.Model):
    cualitativa = models.ForeignKey('Cualitativa', on_delete=models.CASCADE)
    opcion = models.ForeignKey('Opcion', on_delete=models.CASCADE)

    def __str__(self):
        return ('%s ---> %s' % (str(self.cualitativa),  str(self.opcion))) 

    class Meta():
        verbose_name_plural = 'CualitativaOpciones'
        db_table = 'gest_lab_cualitativa_opcion'


class ResultadoCualitativo(models.Model):
    solicitud = models.ForeignKey('Solicitud', on_delete=models.CASCADE)
    cualitativa_opcion = models.ForeignKey('CualitativaOpcion', on_delete=models.CASCADE)
    
    def __str__(self):
        return ('%s ---> %s' % (str(self.solicitud),  str(self.cualitativa_opcion))) 
    
    class Meta():
        verbose_name_plural = 'ResultadosCualitativos'


class ResultadoCuantitativo(models.Model):
    solicitud = models.ForeignKey('Solicitud', on_delete=models.CASCADE)
    valor = models.FloatField()
    
    class Meta():
        verbose_name_plural = 'ResultadosCuantitativos'


class ResultadoDescriptivo(models.Model):
    solicitud = models.ForeignKey('Solicitud', on_delete=models.CASCADE)
    resultado = models.TextField()

    class Meta():
        verbose_name_plural = 'ResultadosDescriptivos'

# class examen_prueba(models.Model):
#     examen = models.ForeignKey('examen', on_delete=models.CASCADE)
#     prueba = models.ForeignKey('prueba', on_delete=models.CASCADE)
#     def __str__(self):
#         return ('%s ---> %s' % (str(self.examen),  str(self.prueba))) 

# class insumo_prueba(models.Model):
#     insumo = models.ForeignKey('insumo', on_delete=models.CASCADE)
#     prueba = models.ForeignKey('prueba', on_delete=models.CASCADE)
#     def __str__(self):
#         return ('%s ---> %s' % (str(self.insumo),  str(self.prueba)))