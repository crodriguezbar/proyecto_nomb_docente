from django.urls import path
from app_nomb_doc.views import *

urlpatterns = [
    path('', inicio, name='home'),
    #DOCENTES
    path('altadocente/', alta_docente, name='altadocente'), 
    path('reporte/', repor_alta_docente, name='reportealtadocente'), 
    path('reporte_dni/', repor_alta_docente_dni, name='reportealtadocentedni'),
    #CARRERAS
    path('altacarrera/', alta_carrera, name='altacarrera'), 
    path('reportecarreras/', reporte_carrera, name='reportealtacarerras'),
    #COMISIONES
    path('altacomision/', alta_comision, name='altacomision'),
    path('reportecomision/', reporte_comisiones, name='reportecomision'),
]