from django.shortcuts import render, redirect
from app_nomb_doc.models import Carreras, Comisiones, Docentes
from app_nomb_doc.forms import FormAltaCarrera, FormAltaComisiones, FormAltaDocente, FormReporte, FormReporteCarrera, FormReporteComisiones, FormReporteDni

# Create your views here.

def inicio (request):
    return render(request, 'plantillas/home.html')

#DOCENTES
def alta_docente (request):
    if request.method == 'POST':
        f_alta_docente=FormAltaDocente(request.POST)
        
        if f_alta_docente.is_valid():
            data = f_alta_docente.cleaned_data
            alta_docente1=Docentes(nombre=data.get('nombre'), apellido=data.get('apellido'), dni=data.get('dni'), titulo_grado=data.get('titulo_grado'), hs_asignar=data.get('hs_asignar'), metodo_alta=data.get('metodo_alta'), fecha_alta=data.get('fecha_alta'))
            alta_docente1.save()    
            return render(request, 'formularios/docentes/form_alta_docente.html', {'formulario':FormAltaDocente(), 'registrado':'OK', 'docente_registrado': alta_docente1})
    contexto={
        'formulario':FormAltaDocente(),
        'registrado':''
    }
    return render(request, 'formularios/docentes/form_alta_docente.html', contexto) 

def repor_alta_docente(request):
    if request.method == 'GET':
        r_alta_docente=FormReporte(request.GET)   
        if r_alta_docente.is_valid():
            desde_fecha_alta=request.GET.get('desde_fecha_alta')
            hasta_fecha_alta=request.GET.get('hasta_fecha_alta')
            docentes=Docentes.objects.filter(fecha_alta__gte=desde_fecha_alta, fecha_alta__lte=hasta_fecha_alta)
            contexto={
                'formulario': FormReporte(),
                'docentes':docentes,
            }
            return render(request, 'formularios/docentes/reporte_alta_docente.html', contexto) 
    contexto={
        'formulario':FormReporte(),
        }
    return render(request, 'formularios/docentes/reporte_alta_docente.html',contexto)

def repor_alta_docente_dni(request):
    if request.method == 'GET':
        r_alta_docente_dni=FormReporteDni(request.GET)   
        if r_alta_docente_dni.is_valid():
            dni=request.GET.get('dni')
            docentes=Docentes.objects.filter(dni__icontains=dni)
            contexto={
                'formulario': FormReporteDni(),
                'docentes':docentes,
            }
            return render(request, 'formularios/docentes/reporte_alta_docente_dni.html', contexto) 
    contexto={
        'formulario':FormReporteDni(),
    }
    return render(request, 'formularios/docentes/reporte_alta_docente_dni.html',contexto)

#CARRERAS
def alta_carrera(request):
    if request.method == 'POST':
        f_alta_carrera=FormAltaCarrera(request.POST)
        
        if f_alta_carrera.is_valid():
            data = f_alta_carrera.cleaned_data
            alta_carrera1=Carreras(carrera=data.get('carrera'), codigo=data.get('codigo'), tipo_carrera=data.get('tipo_carrera'), plan_de_estudio=data.get('plan_de_estudio'), resolucion_rectoral=data.get('resolucion_rectoral'), cantidad_asignaturas=data.get('cantidad_asignaturas'))
            alta_carrera1.save()    
            return render(request, 'formularios/carreras/form_alta_carrera.html', {'formulario':FormAltaCarrera(), 'registro':'OK', 'carrera_registrada': alta_carrera1})
    contexto={
        'formulario':FormAltaCarrera(),
        'registro':''
    }
    return render(request, 'formularios/carreras/form_alta_carrera.html', contexto)

def reporte_carrera(request):
    if request.method == 'GET':
        r_carrera=FormReporteCarrera(request.GET)   
        if r_carrera.is_valid():
            carrera=request.GET.get('carrera')
            carrera=Carreras.objects.filter(carrera__icontains=carrera)
            contexto={
                'formulario': FormReporteCarrera(),
                'carreras':carrera,
            }
            return render(request, 'formularios/carreras/reporte_carreras.html', contexto) 
    contexto={
        'formulario':FormReporteCarrera(),
    }
    return render(request, 'formularios/carreras/reporte_carreras.html',contexto) 

#COMISIONES
def alta_comision(request):
    if request.method == 'POST':
        f_alta_comisiones=FormAltaComisiones(request.POST)
        if f_alta_comisiones.is_valid():
            data = f_alta_comisiones.cleaned_data
            alta_comision1=Comisiones(codigo=data.get('codigo'), comision=data.get('comision'), modalidad=data.get('modalidad'), horario=data.get('horario'))
            alta_comision1.save()    
            return render(request, 'formularios/comisiones/form_alta_comision.html', {'formulario':FormAltaComisiones(), 'registro':'OK', 'comision_registrada': alta_comision1})
    contexto={
        'formulario':FormAltaComisiones(),
        'registro':''
    }
    return render(request, 'formularios/comisiones/form_alta_comision.html', contexto)

def reporte_comisiones(request):
    if request.method == 'GET':
        r_comisiones=FormReporteComisiones(request.GET)   
        if r_comisiones.is_valid():
            comision=request.GET.get('comision')
            comision=Comisiones.objects.filter(carrera__icontains=comision)
            contexto={
                'formulario': FormReporteComisiones(),
                'comisiones':comision,
            }
            return render(request, 'formularios/comisiones/reporte_comisiones.html', contexto) 
    contexto={
        'formulario':FormReporteComisiones(),
    }
    return render(request, 'formularios/comisiones/reporte_comisiones.html',contexto) 
