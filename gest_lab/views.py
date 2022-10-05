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