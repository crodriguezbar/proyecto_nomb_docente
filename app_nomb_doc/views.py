from django.contrib import messages
from django.shortcuts import render, redirect
from app_nomb_doc.models import Asignatura, Carreras, Comisiones, Docentes
from app_nomb_doc.forms import AltaAsignaturas, FormAltaCarrera, FormAltaComisiones, FormAltaDocente, FormReporteCarrera, FormReporteComisiones, FormReporteDocente

# Create your views here.

def inicio (request):
    return render(request, 'plantillas/home.html')

#DOCENTES
def alta_docente (request):
    formulario=FormAltaDocente (request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El docente ha sido registrado exitosamente.!')
        return redirect ('/altadocente')
    contexto={
        'formulario': formulario,
    }
    return render(request, 'formularios/docentes/form_alta_docente.html', contexto)
    
def reporte_docente(request):
    if request.method == 'GET':
        r_alta_docente=FormReporteDocente(request.GET)   
        if r_alta_docente.is_valid():
            desde_fecha_alta=request.GET.get('desde_fecha_alta')
            hasta_fecha_alta=request.GET.get('hasta_fecha_alta')
            docentes=Docentes.objects.filter(fecha_alta__gte=desde_fecha_alta, fecha_alta__lte=hasta_fecha_alta)
            contexto={
                'formulario': FormReporteDocente(),
                'docentes':docentes,
            }
            return render(request, 'formularios/docentes/reporte_docente.html', contexto) 
    contexto={
        'formulario':FormReporteDocente(),
        }
    return render(request, 'formularios/docentes/reporte_docente.html',contexto)

#CARRERAS
def alta_carrera(request):
    if request.method == 'POST':
        f_alta_carrera=FormAltaCarrera(request.POST)
        alta_asignaturas=AltaAsignaturas(request.POST)
        
        if f_alta_carrera.is_valid() and alta_asignaturas.is_valid():
            data1 = f_alta_carrera.cleaned_data
            data2 = alta_asignaturas.cleaned_data
            alta_carrera1=Carreras(carrera=data1.get('carrera'), codigo=data1.get('codigo'), tipo_carrera=data1.get('tipo_carrera'), plan_de_estudio=data1.get('plan_de_estudio'), resolucion_rectoral=data1.get('resolucion_rectoral'), cantidad_asignaturas=data1.get('cantidad_asignaturas'))
            alta_asignaturas1=Asignatura(asignatura=data2.get('asignatura'))
            alta_carrera1.save() 
            alta_asignaturas1.save() 
            contexto ={
                'formulario1':FormAltaCarrera(),
                'registro':'OK',
                'carrera_registrada': alta_carrera1,
                'formulario2':AltaAsignaturas(), 
            }   
            return render(request, 'formularios/carreras/form_alta_carrera.html', contexto)
    contexto={
        'formulario1':FormAltaCarrera(),
        'formulario2':AltaAsignaturas(),
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
