from django.shortcuts import render, HttpResponse
from django.template import Context
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
    return render(request, 'gest_lab/validar.html',{'dir_ex':'/validar'})
    
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