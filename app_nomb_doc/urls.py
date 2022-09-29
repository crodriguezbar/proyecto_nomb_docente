from django.urls import path
from app_nomb_doc.views import *

urlpatterns = [
    path('', inicio, name='home'),
    #DOCENTES
    path('altadocente/', alta_docente, name='altadocente'), 
    path('reporte_docente/', reporte_docente, name='reportedocente'), 
    path('eliminar_docente/<dni>', eliminar_docente, name='eliminardocente'),
    path('editar_docente/<dni>', editar_docente, name='editardocente'),
    #CARRERAS
    path('altacarrera/', alta_carrera, name='altacarrera'), 
    path('altaasignaturas/', alta_asignaturas, name='altaasignaturas'), 
    path('reportecarreras/', reporte_carrera, name='reportecarreras'),
    path('reporteasignaturas/', reporte_asignaturas, name='reporteasignaturas'),
    path('eliminar_carrera/<id>', eliminar_carrera, name='eliminarcarrera'),
    path('editar_carrera/<id>', editar_carrera, name='editarcarrera'),
    path('listar_asignaturas/<id>', listar_asignaturas, name='listarasignaturas'),
    #COMISIONES
    path('altacomision/', alta_comision, name='altacomision'),
    path('reportecomision/', reporte_comisiones, name='reportecomision'),
]