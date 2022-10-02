from django.contrib import messages
from django.shortcuts import render, redirect
from app_nomb_doc.models import Carreras, Comisiones, Docentes, Asignaturas
from app_nomb_doc.forms import FormAltaCarrera, FormAltaComisiones, FormAltaDocente, FormAnioSemestre, FormAsignaturas, FormCodigo, FormReporteAsignatura, FormReporteCarrera, FormReporteComisiones, FormReporteDocente
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory


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
        return redirect ('/alta_docente')
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
        if all([dni =="", desde_fecha_alta=="", hasta_fecha_alta==""]):
            return redirect('reportedocente')
        elif dni =="" and desde_fecha_alta=="":
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
        formulario=FormAltaDocente(request.POST, instance=docente_editar)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Los datos del docente %s, %s (%s) han sido actualizados exitosamente.!' % (docente_editar.apellido, docente_editar.nombre, docente_editar.dni))
            return redirect('reportedocente')
        messages.info(request, 'Ningun campo puede estar vacio!') 
    contexto={
        'formulario':FormAltaDocente(
            instance=docente_editar
        )
    }
    return render(request, 'formularios/docentes/form_alta_docente.html', contexto)

#CARRERAS
#Carreras
@login_required
def alta_carrera (request):
    formulario=FormAltaCarrera (request.POST or None)
    if formulario.is_valid():
        data=formulario.cleaned_data
        alta_carrera=Carreras(
            carrera=data.get('carrera'), 
            codigo=data.get('codigo'), 
            tipo_carrera=data.get('tipo_carrera'),
            plan_de_estudio=data.get('plan_de_estudio'),
            resolucion_rectoral=data.get('resolucion_rectoral'),
            cantidad_asignaturas=data.get('cantidad_asignaturas'), 
        )
        alta_carrera.save()
        messages.success(request, 
            'La Carrera %s (Plan de estudio: %s) ha sido registrada exitosamente.!' 
            % (alta_carrera.carrera, alta_carrera.plan_de_estudio)
        )
        return redirect ('/altacarrera')
    contexto={
        'formulario': formulario,
    }
    return render(request, 'formularios/carreras/form_alta_carrera.html', contexto)

def reporte_carrera(request):
    reporte_carrera=Carreras.objects.all().order_by('carrera', 'plan_de_estudio').values()
    return render(request, 'formularios/carreras/reporte_carreras.html', {'reporte_carrera': reporte_carrera})

@login_required   
def eliminar_carrera (request, id): 
    carrera_eliminar=Carreras.objects.get(id=id)
    messages.success(request, "La carrera %s (%s) fue eliminada" % (carrera_eliminar.carrera, carrera_eliminar.plan_de_estudio))
    carrera_eliminar.delete() 
    return redirect('reportecarreras')

@login_required
def editar_carrera (request, id): 
    carrera_editar=Carreras.objects.get(id=id)
    if request.method == 'POST':
        formulario=FormAltaCarrera(request.POST, instance=carrera_editar)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Los datos de la carrera %s (%s) han sido actualizados exitosamente.!' % (carrera_editar.carrera, carrera_editar.plan_de_estudio))
            return redirect('reportecarreras')
        messages.info(request, 'Ningun campo puede estar vacio!') 
    contexto={
        'formulario':FormAltaCarrera(
            instance=carrera_editar),  
    }
    return render(request, 'formularios/carreras/form_alta_carrera.html', contexto)

#Asignaturas
@login_required
def alta_asignaturas (request):
    formulario=FormCodigo (request.POST or None)
    anio_semestre_formset=formset_factory(FormAnioSemestre,extra=0)
    formulario1=anio_semestre_formset (request.POST or None)
    asignatura_formset=formset_factory(FormAsignaturas,extra=0)
    formulario2=asignatura_formset (request.POST or None)
    if request.method == 'POST':
        print(request.POST)
    if all([formulario.is_valid(), formulario1.is_valid(), formulario.is_valid()]):
        carrera=formulario.cleaned_data
        data1=formulario1.cleaned_data
        data2=formulario2.cleaned_data
        print(carrera,data1,data2)
        alta_asignatura=Asignaturas(codigo=carrera.get('codigo'))
        for anio_semestre in data1:
            alta_asignatura=Asignaturas(anio_semestre=anio_semestre.get('anio_semestre'))
            for asignatura in data2:
                alta_asignatura=Asignaturas(asignatura=asignatura.get('asignatura'))
                alta_asignatura.save()
        messages.success(request, 
            'Las asignaturas de la carrera ¡¡¡FALTA!!! han sido registradas exitosamente.!' 
        )
        return redirect ('/alta_asignaturas')
    contexto={
        'formulario': formulario,
        'formulario1': formulario1,
        'formulario2': formulario2,
    }
    return render(request, 'formularios/carreras/form_alta_asignaturas.html', contexto)

def reporte_asignaturas (request):
    formulario=FormReporteAsignatura(request.GET or None)   
    if formulario.is_valid():
        codigo=request.GET.get('codigo')
        if codigo =="":
            return redirect('reporteasignaturas')
        asignaturas=Asignaturas.objects.filter(codigo__contain=codigo) 
        messages.info(request, "CRITERIO DE BUSQUEDA: hasta el %s" % (codigo))       
        contexto={
            'formulario': FormReporteAsignatura(),
            'asignaturas':asignaturas,
        }
        return render(request, 'formularios/carreras/reporte_asignaturas.html', contexto) 
    contexto={
        'formulario':FormReporteAsignatura(),
        }
    return render(request, 'formularios/carreras/reporte_asignaturas.html', contexto) 

@login_required
def eliminar_asignaturas (request, id):
    pass

@login_required
def editar_asignaturas (request, id):
    pass

#COMISIONES
@login_required
def alta_comision(request):
    f_alta_comisiones=FormAltaComisiones(request.POST or None)
    if f_alta_comisiones.is_valid():
        data=f_alta_comisiones.cleaned_data
        alta_comision=Comisiones(
            anio_academico=data.get('anio_academico'), 
            semestre_academico=data.get('semestre_academico'), 
            comision=data.get('comision'),
            modalidad=data.get('modalidad'),
            horario=data.get('horario'),
            codigo=data.get('codigo'), 
            asignatura=data.get('asignatura'),
        )
        alta_comision.save()
        messages.success(request, 
            'La comision %s (Carrera: %s, Asignatura: %s, Modalidad: %s, Horario: %s) ha sido registrada exitosamente.!' 
            % (alta_comision.comision, alta_comision.codigo, alta_comision.asignatura, alta_comision.modalidad, alta_comision.horario)
        )
        return redirect('altacomision')
    contexto={
        'formulario':FormAltaComisiones(),
    }
    return render(request, 'formularios/comisiones/form_alta_comision.html', contexto)

def cargar_asignaturas (request):
    codigo_id = request.GET.get('codigo_id')
    asignaturas = Asignaturas.objects.filter(codigo_id=codigo_id).all()
    print(asignaturas)
    return render(request, 'formularios/comisiones/asignaturas_lista_opciones.html', {'asignaturas': asignaturas})

@login_required   
def reporte_comisiones(request):
    reporte_comisiones = Comisiones.objects.all().order_by('codigo', 'anio_academico','semestre_academico','modalidad','comision').values()
    return render(request, 'formularios/comisiones/reporte_comisiones.html', {'comisiones' : reporte_comisiones})

@login_required   
def eliminar_comision (request, id): 
    comision_eliminar=Comisiones.objects.get(id=id)
    messages.success(request, "La comision %s (%s, %s) fue eliminada" % (comision_eliminar.comision, comision_eliminar.codigo, comision_eliminar.asignatura))
    comision_eliminar.delete() 
    return redirect('reportecomision')

@login_required
def editar_comision (request, id): 
    comision_editar=Comisiones.objects.get(id=id)
    if request.method == 'POST':
        formulario=FormAltaComisiones(request.POST, instance=comision_editar)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Los datos de la comision %s (%s) han sido actualizados exitosamente.!' % (comision_editar.comision, comision_editar.codigo, comision_editar.asignatura))
            return redirect('reportecomision')
        messages.info(request, 'Ningun campo puede estar vacio!') 
    contexto={
        'formulario':FormAltaComisiones(
            instance=comision_editar),  
    }
    return render(request, 'formularios/carreras/form_alta_carrera.html', contexto)




