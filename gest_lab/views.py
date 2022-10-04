from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('inicio')

def registrar(request):
    return HttpResponse('registrar')

def procesar(request):
    return HttpResponse('procesar')

def validar(request):
    return HttpResponse('validar')

def entregar(request):
    return HttpResponse('entregar')