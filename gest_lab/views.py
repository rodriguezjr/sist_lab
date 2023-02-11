from django.shortcuts import render, HttpResponse
from django.template import Context
from gest_lab.models import Cliente, Sexo, Solicitud, Prueba, Examen, Categoria
from gest_lab.forms import FormularioCliente, FormularioMineria
import datetime
from django.db.models import Count
from gest_lab.static.evaluar_modelo import evaluacion
# Create your views here.

def Inicio(request):
    #return HttpResponse('inicio')
    fecha_dt = datetime.date.today()
    l_solicitud = Solicitud.objects.values('n_orden').filter(f_solicitud__date = fecha_dt).annotate(dcount=Count('n_orden')).order_by()
    p_procesar = Solicitud.objects.values('n_orden').filter(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
    p_validar = Solicitud.objects.values('n_orden').filter(f_validado=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
    p_entregar = Solicitud.objects.values('n_orden').filter(f_entrega=None).exclude(f_validado=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
    
    c_examenes={
        'l_solicitud':len(l_solicitud),
        'p_procesar':len(p_procesar),
        'p_validar':len(p_validar),
        'p_entregar':len(p_entregar)
    }
    return render(request, 'gest_lab/inicio.html',{'c_examenes':c_examenes})


def Solicitar(request):
    #return HttpResponse('solicitar')
    form = FormularioCliente()
    if request.method == 'POST':
        form = FormularioCliente(request.POST)
        if form.is_valid():
            cli = form.save()
            cli.save()
    else:
        form = FormularioCliente()

    persona = {}
    l_examen = {}
    l_categoria = {}
    if request.method == 'GET':
        if len(persona) == 0:
            persona = Cliente.objects.filter(cedula=request.GET.get('cedula_text')).values()
            l_examen = Examen.objects.all()
            l_categoria = Categoria.objects.all()
    else:
        persona = {}

    fecha_dt = datetime.datetime.now()
    for x in persona:
        x['edad'] = fecha_dt.year - x['f_nac'].year - ((fecha_dt.month,fecha_dt.day) < (x['f_nac'].month,x['f_nac'].day))
    fecha = fecha_dt.strftime("%Y-%m-%d %H:%M")
    n_orden = fecha_dt.strftime("%y%m%d") + ("-01")

    return render(request, 'gest_lab/solicitar.html',{'POST':request.POST,'cli':persona, 'fecha':fecha, 'form':form, 'examenes':l_examen, 'categorias':l_categoria, 'n_orden':n_orden})
   
def Procesar(request):
    #return HttpResponse('procesar')
    l_examen = Examen.objects.all()
    l_test = Solicitud.objects.values('examen_id','examen__nombre').filter(f_validado=None,f_entrega=None).annotate(dcount=Count('n_orden')).order_by()
    print(l_test)
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

    return render(request, 'gest_lab/procesar.html',{'dir_ex':'/procesar', 'solicitud':l_solicitud, 'examenes':l_test})
    
def Validar(request):
    #return HttpResponse('validar')
    l_examen = Examen.objects.all()
    l_test = Solicitud.objects.values('examen_id','examen__nombre').filter(f_validado=None,f_entrega=None).exclude(f_proceso=None).annotate(dcount=Count('n_orden')).order_by()
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
    return render(request, 'gest_lab/validar.html',{'dir_ex':'/validar', 'solicitud':l_solicitud, 'examenes':l_test})

    
def Entregar(request):
    #return HttpResponse('entregar')
    l_examen = Examen.objects.all()
    l_test = Solicitud.objects.values('examen_id','examen__nombre').filter(f_entrega=None).exclude(f_proceso=None).exclude(f_validado=None).annotate(dcount=Count('n_orden')).order_by()
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
    return render(request, 'gest_lab/entregar.html',{'dir_res':'/entregar', 'solicitud':l_solicitud, 'examenes':l_test})

    
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

def Login(request):
    return render(request, 'gest_lab/login.html')

def Mineria(request):
    resultado = []
    form = FormularioMineria()
    if request.method == 'GET':
        form = FormularioMineria(request.GET)
        if form.is_valid():
            Edad = request.GET.get('Edad')
            Linfocitos = request.GET.get('Linfocitos')
            MID = request.GET.get('MID')
            Neutrofilos = request.GET.get('Neutrofilos')
            Leucocitos = request.GET.get('Leucocitos')
            Eritrocitos = request.GET.get('Eritrocitos')
            Hemoglobina = request.GET.get('Hemoglobina')
            Hematocritos = request.GET.get('Hematocritos')
            MCV = request.GET.get('MCV')
            MCH = request.GET.get('MCH')
            MCHC = request.GET.get('MCHC')
            Plaquetas = request.GET.get('Plaquetas')
            MPV = request.GET.get('MPV')
            datos = [Edad, Linfocitos, MID, Neutrofilos, Leucocitos, Eritrocitos, Hemoglobina, Hematocritos, MCV, MCH, MCHC, Plaquetas, MPV]
            resultado = evaluacion(datos)
    else:
        form = FormularioMineria()



    return render(request, 'gest_lab/mineria.html', {'form':form, 'resultado':resultado})

def Examenes(request):
    l_examen = Examen.objects.all()
    l_categorias = Categoria.objects.all()
    l_pruebas = Prueba.objects.all()

    l_ex = Prueba.objects.values('categoria__nombre','examen__nombre','examen__precio').annotate(dcount=Count('examen__nombre')).order_by()


    return render(request, 'gest_lab/examenes.html', {'l_examen':l_examen,'l_categorias':l_categorias,'l_pruebas':l_pruebas, 'l_ex':l_ex})