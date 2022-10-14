from django.shortcuts import render, HttpResponse
from django.template import Context
from gest_lab.models import cliente, sexo
import datetime
# Create your views here.

def inicio(request):
    #return HttpResponse('inicio')
    return render(request, 'gest_lab/inicio.html')

def solicitar(request):
    #return HttpResponse('solicitar')
    return render(request, 'gest_lab/solicitar.html',{'dir_ex':'/solicitar'})
    
def procesar(request):
    #return HttpResponse('procesar')
    return render(request, 'gest_lab/procesar.html',{'dir_ex':'/procesar'})
    
def validar(request):
    #return HttpResponse('validar')
    cli = {}
    if request.method == 'POST':
        cli = cliente.objects.filter(cedula=request.POST['text_cedula']).values()
        if len(cli) == 0:
            c = cliente(cedula=request.POST['text_cedula'],
                        nombre=request.POST['text_nombre_cliente'],
                        apellido=request.POST['text_apellido_cliente'],
                        f_nac=request.POST['text_fecha_nacimiento'],
                        direccion=request.POST['text_direccion_cliente'],
                        telefono=request.POST['text_telefono_cliente'],
                        id_sexo= sexo.objects.get(id=request.POST['radio_sexo'])
                        )
            c.save()

    anio = datetime.datetime.now()
    edad = 0
    for x in cli:
        edad = anio.year - x['f_nac'].year
    anio2 = anio.strftime("%Y-%m-%d %H:%M")


    return render(request, 'gest_lab/validar.html',{'dir_ex':'/validar','cli':cli, 'edad':edad, 'anio':anio2})
    
def entregar(request):
    #return HttpResponse('entregar')
    return render(request, 'gest_lab/entregar.html',{'dir_ex':'/entregar'})
    
def configuracion(request):
    #return HttpResponse('configuracion')
    return render(request, 'gest_lab/configuracion.html')

def pacientes(request):
    #return HttpResponse('pacientes')
    return render(request, 'gest_lab/pacientes.html')

def examenes(request):
    #return HttpResponse('examenes')
    return render(request, 'gest_lab/examenes.html',{'dir_conf':'/examenes'})

def insumos(request):
    #return HttpResponse('insumos')
    return render(request, 'gest_lab/insumos.html',{'dir_conf':'/insumos'})

def base(request):
    #return HttpResponse('insumos')
    direcciones = ['solicitar','procesar','validar','entregar']
    return render(request, 'gest_lab/base.html', context={'arr':direcciones})