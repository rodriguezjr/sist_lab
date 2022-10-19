from django.shortcuts import render, HttpResponse
from django.template import Context
from gest_lab.models import cliente, sexo, analisis, examen
from gest_lab.forms import FormularioCliente
import datetime
from django.db.models import Count
# Create your views here.

def inicio(request):
    #return HttpResponse('inicio')
    return render(request, 'gest_lab/inicio.html')

def solicitar(request):
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
            persona = cliente.objects.filter(cedula=request.GET.get('cedula_text')).values()
            #print(request.GET.get('cedula_text'))
    else:
        persona = {}

    fecha_dt = datetime.datetime.now()
    for x in persona:
        x['edad'] = fecha_dt.year - x['f_nac'].year
    fecha = fecha_dt.strftime("%Y-%m-%d %H:%M")

    return render(request, 'gest_lab/solicitar.html',{'dir_ex':'/solicitar','cli':persona, 'fecha':fecha})
   
def procesar(request):
    #return HttpResponse('procesar')
    l_analisis = analisis.objects.all()
    l_examenes = examen.objects.all()
    null = None

    if request.method == 'GET':
        ced = request.GET.get('cedula') if request.GET.get('cedula') != None else ''
        n_ord = request.GET.get('n_orden') if request.GET.get('n_orden') != None else ''
        t_ex = request.GET.get('t_examen') if request.GET.get('t_examen') != None else 0
        if t_ex == 0:
            l_examenes = examen.objects.values('n_orden','id_cliente__cedula','id_analisis__nombre').filter(id_cliente__cedula__startswith=ced,n_orden__endswith=n_ord,f_proceso=None,f_validado=None,f_entrega=None).annotate(dcount=Count('n_orden')).order_by()
        else:
            l_examenes = examen.objects.values('n_orden','id_cliente__cedula','id_analisis__nombre').filter(id_cliente__cedula__startswith=ced,n_orden__endswith=n_ord,id_analisis=t_ex,f_proceso=None,f_validado=None,f_entrega=None).annotate(dcount=Count('n_orden')).order_by()
    
    else:
        l_examenes = examen.objects.all()
    
    print(l_examenes)
    return render(request, 'gest_lab/procesar.html',{'dir_ex':'/procesar', 'analisis':l_analisis, 'examenes':l_examenes})
    
def validar(request):
    #return HttpResponse('validar')
    l_analisis = analisis.objects.all()
    l_examenes = examen.objects.all()
    if request.method == 'GET':
        ced = request.GET.get('cedula') if request.GET.get('cedula') != None else ''
        n_ord = request.GET.get('n_orden') if request.GET.get('n_orden') != None else ''
        t_ex = request.GET.get('t_examen') if request.GET.get('t_examen') != None else 0
        if t_ex == 0:
            l_examenes = examen.objects.values('n_orden','id_cliente__cedula','id_analisis__nombre').filter(id_cliente__cedula__startswith=ced,n_orden__endswith=n_ord,f_validado=None,f_entrega=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        else:
            l_examenes = examen.objects.values('n_orden','id_cliente__cedula','id_analisis__nombre').filter(id_cliente__cedula__startswith=ced,n_orden__endswith=n_ord,id_analisis=t_ex,f_validado=None,f_entrega=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        # print(l_examenes.query)
    return render(request, 'gest_lab/validar.html',{'dir_ex':'/procesar', 'analisis':l_analisis, 'l_examenes':l_examenes})

    
def entregar(request):
    #return HttpResponse('entregar')
    l_analisis = analisis.objects.all()
    l_examenes = examen.objects.all()
    if request.method == 'GET':
        ced = request.GET.get('cedula') if request.GET.get('cedula') != None else ''
        n_ord = request.GET.get('n_orden') if request.GET.get('n_orden') != None else ''
        t_ex = request.GET.get('t_examen') if request.GET.get('t_examen') != None else 0
        if t_ex == 0:
            l_examenes = examen.objects.values('n_orden','id_cliente__cedula','id_analisis__nombre').filter(id_cliente__cedula__startswith=ced,n_orden__endswith=n_ord,f_entrega=None).exclude(f_validado=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        else:
            l_examenes = examen.objects.values('n_orden','id_cliente__cedula','id_analisis__nombre').filter(id_cliente__cedula__startswith=ced,n_orden__endswith=n_ord,id_analisis=t_ex,f_entrega=None).exclude(f_validado=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
        # print(l_examenes.query)
    return render(request, 'gest_lab/entregar.html',{'dir_ex':'/procesar', 'analisis':l_analisis, 'l_examenes':l_examenes, 'query':l_examenes.query})

    
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