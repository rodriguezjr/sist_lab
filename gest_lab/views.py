from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('inicio')

def solicitar(request):
    return HttpResponse('solicitar')

def procesar(request):
    return HttpResponse('procesar')

def validar(request):
    return HttpResponse('validar')

def entregar(request):
    return HttpResponse('entregar')

def configuracion(request):
    return HttpResponse('configuracion')