from django.urls import path
from app_nomb_doc.views import *

urlpatterns = [
    path('', inicio, name='home'),
    #DOCENTES
    path('alta_docente/', alta_docente, name='altadocente'), 
    path('reporte_docente/', reporte_docente, name='reportedocente'), 
    path('eliminar_docente/<dni>', eliminar_docente, name='eliminardocente'),
    path('editar_docente/<dni>', editar_docente, name='editardocente'),
    
    #CARRERAS
    #Carreras
    path('alta_carrera/', alta_carrera, name='altacarrera'), 
    path('reporte_carreras/', reporte_carrera, name='reportecarreras'),
    path('eliminar_carrera/<id>', eliminar_carrera, name='eliminarcarrera'),
    path('editar_carrera/<id>', editar_carrera, name='editarcarrera'),
    #Asignaturas
    path('alta_asignaturas/', alta_asignaturas, name='altaasignaturas'),
    path('reporte_asignaturas/', reporte_asignaturas, name='reporteasignaturas'), 
    path('eliminar_asignaturas/<id>', eliminar_carrera, name='eliminarasignaturas'),
    path('editar_asignaturas/<id>', editar_carrera, name='editarasignaturas'),
    
    #COMISIONES
    path('alta_comision/', alta_comision, name='altacomision'),
    path('reporte_comision/', reporte_comisiones, name='reportecomision'),
    path('ajax/cargar_asignaturas/', cargar_asignaturas, name='ajaxcargarasignaturas'),
]