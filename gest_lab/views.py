from django.shortcuts import render, HttpResponse
from django.template import Context
from gest_lab.models import Cliente, Sexo, Solicitud, Prueba, Examen
from gest_lab.forms import FormularioCliente
import datetime
from django.db.models import Count
# Create your views here.

def Inicio(request):
    #return HttpResponse('inicio')
    return render(request, 'gest_lab/inicio.html')

def Solicitar(request):
    #return HttpResponse('solicitar')
    #form = FormularioCliente()
    # if request.method == 'POST':
    #     form = FormularioCliente(request.POST)
    #     if form.is_valid():
    #         cli = form.save()
    #         cli.save()
    # else:
    #     form = FormularioCliente()
    persona = {}
    if request.method == 'GET':
        if len(persona) == 0:
            persona = Cliente.objects.filter(cedula=request.GET.get('cedula_text')).values()
            #print(request.GET.get('cedula_text'))
    else:
        persona = {}

    fecha_dt = datetime.datetime.now()
    for x in persona:
        x['edad'] = fecha_dt.year - x['f_nac'].year
    fecha = fecha_dt.strftime("%Y-%m-%d %H:%M")

    return render(request, 'gest_lab/solicitar.html',{'dir_ex':'/solicitar','cli':persona, 'fecha':fecha})
   
def Procesar(request):
    #return HttpResponse('procesar')
    l_examen = Examen.objects.all()
    l_solicitud = Solicitud.objects.all()
    null = None

    if request.method == 'GET':
        ced = request.GET.get('cedula') if request.GET.get('cedula') != None else ''
        n_ord = request.GET.get('n_orden') if request.GET.get('n_orden') != None else ''
        t_ex = request.GET.get('t_examen') if request.GET.get('t_examen') != None else ''
        print('el valor de t_ex es ', t_ex)
        if t_ex == '':
            l_solicitud = Solicitud.objects.values('n_orden','cliente__cedula','examen__nombre').filter(cliente__cedula__startswith=ced,n_orden__endswith=n_ord,f_proceso=None,f_validado=None,f_entrega=None).annotate(dcount=Count('n_orden')).order_by()
        else:
            l_solicitud = Solicitud.objects.values('n_orden','cliente__cedula','examen__nombre').filter(cliente__cedula__startswith=ced,n_orden__endswith=n_ord,examen_id=t_ex,f_proceso=None,f_validado=None,f_entrega=None).annotate(dcount=Count('n_orden')).order_by()
    
    else:
        l_solicitud = Solicitud.objects.all()

    return render(request, 'gest_lab/procesar.html',{'dir_ex':'/procesar', 'solicitud':l_solicitud, 'examenes':l_examen})
    
def Validar(request):
    #return HttpResponse('validar')
    l_examen = Examen.objects.all()
    l_solicitud = Solicitud.objects.all()
    if request.method == 'GET':
        ced = request.GET.get('cedula') if request.GET.get('cedula') != None else ''
        n_ord = request.GET.get('n_orden') if request.GET.get('n_orden') != None else ''
        t_ex = request.GET.get('t_examen') if request.GET.get('t_examen') != None else 0
        if t_ex == 0:
            l_solicitud = Solicitud.objects.values('n_orden','cliente__cedula','examen__nombre').filter(cliente__cedula__startswith=ced,n_orden__endswith=n_ord,f_validado=None,f_entrega=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        else:
            l_solicitud = Solicitud.objects.values('n_orden','cliente__cedula','examen__nombre').filter(cliente__cedula__startswith=ced,n_orden__endswith=n_ord,examen_id=t_ex,f_validado=None,f_entrega=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        # print(l_solicitud.query)
    return render(request, 'gest_lab/validar.html',{'dir_ex':'/procesar', 'solicitud':l_solicitud, 'examenes':l_examen})

    
def Entregar(request):
    #return HttpResponse('entregar')
    l_examen = Examen.objects.all()
    l_solicitud = Solicitud.objects.all()
    if request.method == 'GET':
        ced = request.GET.get('cedula') if request.GET.get('cedula') != None else ''
        n_ord = request.GET.get('n_orden') if request.GET.get('n_orden') != None else ''
        t_ex = request.GET.get('t_examen') if request.GET.get('t_examen') != None else 0
        if t_ex == 0:
            l_solicitud = Solicitud.objects.values('n_orden','cliente__cedula','examen__nombre').filter(cliente__cedula__startswith=ced,n_orden__endswith=n_ord,f_entrega=None).exclude(f_validado=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        else:
            l_solicitud = Solicitud.objects.values('n_orden','cliente__cedula','examen__nombre').filter(cliente__cedula__startswith=ced,n_orden__endswith=n_ord,examen_id=t_ex,f_entrega=None).exclude(f_validado=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        # print(l_solicitud.query)
    return render(request, 'gest_lab/entregar.html',{'dir_ex':'/procesar', 'solicitud':l_solicitud, 'examenes':l_examen})

    
def Configuracion(request):
    #return HttpResponse('configuracion')
    return render(request, 'gest_lab/configuracion.html')

def Pacientes(request):
    #return HttpResponse('pacientes')
    return render(request, 'gest_lab/pacientes.html')

# def Solicitudes(request):
#     #return HttpResponse('solicitudes')
#     return render(request, 'gest_lab/solicitudes.html',{'dir_conf':'/solicitudes'})

def Insumos(request):
    #return HttpResponse('insumos')
    return render(request, 'gest_lab/insumos.html',{'dir_conf':'/insumos'})

def Solicitudes(request):
    #return HttpResponse('insumos')
    return render(request, 'gest_lab/solicitudes.html',{'dir_conf':'/solicitudes'})

def Base(request):
    #return HttpResponse('insumos')
    direcciones = ['solicitar','procesar','validar','entregar']
    return render(request, 'gest_lab/base.html', context={'arr':direcciones})