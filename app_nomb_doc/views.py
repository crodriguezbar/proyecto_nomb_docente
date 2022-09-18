from django.contrib import messages
from django.shortcuts import render, redirect
from app_nomb_doc.models import Carreras, Comisiones, Docentes
from app_nomb_doc.forms import FormAltaCarrera, FormAltaComisiones, FormAltaDocente, FormReporteCarrera, FormReporteComisiones, FormReporteDocente
from django.views.generic.list import ListView 
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio (request):
    return render(request, 'formularios/usuarios/login.html')

#DOCENTES
@login_required
def alta_docente (request):
    formulario=FormAltaDocente (request.POST or None)
    if formulario.is_valid():
        data=formulario.cleaned_data
        alta_docente1=Docentes(
            nombre=data.get('nombre'), 
            apellido=data.get('apellido'), 
            dni=data.get('dni'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            telefono=data.get('telefono'),
            email=data.get('email'), 
            titulo_grado=data.get('titulo_grado'),
            titulo_posgrado=data.get('titulo_posgrado'), 
            hs_asignar=data.get('hs_asignar'), 
            metodo_alta=data.get('metodo_alta'), 
            fecha_alta=data.get('fecha_alta'),
            fecha_creacion=data.get('fecha_creacion'),
        )
        alta_docente1.save()
        messages.success(request, 'El docente %s, %s (%s) ha sido registrado exitosamente.!' % (alta_docente1.apellido, alta_docente1.nombre, alta_docente1.dni))
        return redirect ('/altadocente')
    contexto={
        'formulario': formulario,
    }
    return render(request, 'formularios/docentes/form_alta_docente.html', contexto)
    
def reporte_docente(request):
    formulario=FormReporteDocente(request.GET or None)   
    if formulario.is_valid():
        dni=request.GET.get('dni')
        desde_fecha_alta=request.GET.get('desde_fecha_alta')
        hasta_fecha_alta=request.GET.get('hasta_fecha_alta')
        if dni =="" and desde_fecha_alta=="":
            docentes=Docentes.objects.filter(fecha_alta__lte=hasta_fecha_alta) 
            messages.info(request, "CRITERIO DE BUSQUEDA: hasta el %s" % (hasta_fecha_alta))
        elif dni =="" and hasta_fecha_alta=="":
            docentes=Docentes.objects.filter(fecha_alta__gte=desde_fecha_alta)
            messages.info(request, "CRITERIO DE BUSQUEDA: desde el %s" % (desde_fecha_alta))
        elif desde_fecha_alta !="" and hasta_fecha_alta !="":
            docentes=Docentes.objects.filter(fecha_alta__gte=desde_fecha_alta, fecha_alta__lte=hasta_fecha_alta)
            messages.info(request, "CRITERIO DE BUSQUEDA: desde %s hasta %s" % (desde_fecha_alta, hasta_fecha_alta))
        else:
            docentes=Docentes.objects.filter(dni__contains=dni)
            messages.info(request, "CRITERIO DE BUSQUEDA: El DNI contiene el numero %s" % (dni))
        contexto={
            'formulario': FormReporteDocente(),
            'docentes':docentes,
        }
        return render(request, 'formularios/docentes/reporte_docente.html', contexto) 
    contexto={
        'formulario':FormReporteDocente(),
        }
    return render(request, 'formularios/docentes/reporte_docente.html',contexto)

@login_required
def eliminar_docente(request, dni):
    docente_eliminar=Docentes.objects.get(dni=dni)
    messages.success(request, "El docente %s, %s (Dni: %s) fue eliminado" % (docente_eliminar.apellido, docente_eliminar.nombre, docente_eliminar.dni))
    docente_eliminar.delete() 
    return redirect('reportedocente')

@login_required
def editar_docente(request, dni):
    docente_editar=Docentes.objects.get(dni=dni)
    
    if request.method == 'POST':
        formulario=FormAltaDocente(request.POST)
        
        if formulario.is_valid():
            data=formulario.cleaned_data
            docente_editar.nombre=data.get('nombre')
            docente_editar.apellido=data.get('apellido') 
            docente_editar.dni=data.get('dni')
            docente_editar.fecha_nacimiento=data.get('fecha_nacimiento')
            docente_editar.telefono=data.get('telefono')
            docente_editar.email=data.get('email')
            docente_editar.titulo_grado=data.get('titulo_grado')
            docente_editar.titulo_posgrado=data.get('titulo_posgrado') 
            docente_editar.hs_asignar=data.get('hs_asignar') 
            docente_editar.metodo_alta=data.get('metodo_alta')
            docente_editar.fecha_alta=data.get('fecha_alta')
            docente_editar.fecha_creacion=data.get('fecha_creacion')
            
            docente_editar.save()
            messages.success(request, 'Los datos del docente %s, %s (%s) han sido actualizados exitosamente.!' % (docente_editar.apellido, docente_editar.nombre, docente_editar.dni))
            return redirect('reportedocente')   
    contexto={
        'formulario':FormAltaDocente(
            initial={
                'nombre': docente_editar.nombre,
                'apellido': docente_editar.apellido,
                'dni': docente_editar.dni,
                'fecha_nacimiento': docente_editar.fecha_nacimiento,
                'telefono': docente_editar.telefono,    
                'email': docente_editar.email,
                'titulo_grado': docente_editar.titulo_grado,
                'titulo_posgrado': docente_editar.titulo_posgrado,
                'hs_asignar': docente_editar.hs_asignar,
                'metodo_alta': docente_editar.metodo_alta,
                'fecha_alta': docente_editar.fecha_alta,
            }
        )
    }
    return render(request, 'formularios/docentes/form_alta_docente.html', contexto)

"""class ReporteDocente(ListView):
    model=Docentes
    template_name: 'reporte_docente.html'
    paginate_by: 5
    def get(self, request, *args, **kwargs):
        dni=request.POST.get('dni')
        dnis=dni.objetcs.filter(dni__contains=dni)
    """

#CARRERAS
@login_required
def alta_carrera(request):
    formulario=FormAltaCarrera(request.POST or None)
    if formulario.is_valid():
        data = formulario.cleaned_data
        alta_carrera1=Carreras(
            carrera=data.get('carrera'), 
            codigo=data.get('codigo'), 
            tipo_carrera=data.get('tipo_carrera'), 
            plan_de_estudio=data.get('plan_de_estudio'), 
            resolucion_rectoral=data.get('resolucion_rectoral'), 
            cantidad_asignaturas=data.get('cantidad_asignaturas'),
            asignatura=data.get('asignatura'),
        )
        alta_carrera1.save() 
        messages.success(request, 'La carrera %s (plan: %s) ha sido registrada exitosamente.!' % (alta_carrera1.carrera, alta_carrera1.plan_de_estudio))
        return redirect ('/altacarrera')
    contexto={
        'formulario':formulario,
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
