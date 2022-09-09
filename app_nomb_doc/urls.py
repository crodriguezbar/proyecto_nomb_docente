from django.urls import path
from app_nomb_doc.views import *

urlpatterns = [
    path('', inicio, name='home'),
    #DOCENTES
    path('altadocente/', alta_docente, name='altadocente'), 
    path('reporte_docente/', reporte_docente, name='reportedocente'), 
    #CARRERAS
    path('altacarrera/', alta_carrera, name='altacarrera'), 
    path('reportecarreras/', reporte_carrera, name='reportealtacarerras'),
    #COMISIONES
    path('altacomision/', alta_comision, name='altacomision'),
    path('reportecomision/', reporte_comisiones, name='reportecomision'),
]