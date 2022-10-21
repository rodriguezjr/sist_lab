"""sist_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from gest_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Inicio, name='inicio'),
    path('solicitar',views.Solicitar, name='solicitar'),
    path('procesar',views.Procesar, name='procesar'),
    path('validar',views.Validar, name='validar'),
    path('entregar',views.Entregar, name='entregar'),
    path('configuracion',views.Configuracion, name='configuracion'),
    path('pacientes',views.Pacientes, name='pacientes'),
    # path('examenes',views.Examenes, name='examenes'),
    path('insumos',views.Insumos, name='insumos'),
    path('base',views.Base, name='base'),

]
