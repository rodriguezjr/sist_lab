from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    #return HttpResponse('inicio')
    return render(request, 'gest_lab/inicio.html')

def solicitar(request):
    #return HttpResponse('solicitar')
    return render(request, 'gest_lab/solicitar.html')
    
def procesar(request):
    #return HttpResponse('procesar')
    return render(request, 'gest_lab/procesar.html')
    
def validar(request):
    #return HttpResponse('validar')
    return render(request, 'gest_lab/validar.html')
    
def entregar(request):
    #return HttpResponse('entregar')
    return render(request, 'gest_lab/entregar.html')
    
def configuracion(request):
    #return HttpResponse('configuracion')
    return render(request, 'gest_lab/configuracion.html')

def pacientes(request):
    #return HttpResponse('pacientes')
    return render(request, 'gest_lab/pacientes.html')

def examenes(request):
    #return HttpResponse('examenes')
    return render(request, 'gest_lab/examenes.html')

def insumos(request):
    #return HttpResponse('insumos')
    return render(request, 'gest_lab/insumos.html')

def base(request):
    #return HttpResponse('insumos')
    arr = ['/solicitar','/procesar','/validar','/entregar']
    return render(request, 'gest_lab/insumos.html', context={'arr': arr})