from dataclasses import fields
from datetime import datetime
from django import forms
from app_nomb_doc.models import Docentes

#FORMULARIOS DOCENTES
class FormAltaDocente (forms.Form):
    OPCIONES_SELECCION = (
        (1, 'Seleccion Docente'),
        (2, 'Necesidad y Urgencia'),    
    )

    nombre=forms.CharField(max_length=40, required=True)
    apellido=forms.CharField(max_length=40, required=True)
    dni=forms.IntegerField(required=True)
    titulo_grado=forms.CharField(max_length=40, required=True)
    titulo_posgrado=forms.CharField(max_length=40)
    hs_asignar=forms.IntegerField(max_value=45, required=True)
    metodo_alta=forms.ChoiceField(
        required=True,
        choices=OPCIONES_SELECCION,
        widget= forms.RadioSelect()
    )
    fecha_alta=forms.DateField(
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
        required=True
    )  

class FormReporte (forms.Form):
    desde_fecha_alta=forms.DateField(
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
        required=True
    )
    hasta_fecha_alta=forms.DateField(
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
        required=True
    )

class FormReporteDni (forms.Form):
    dni=forms.IntegerField(required=True)    
    
#FORMULARIOS CARRERAS
class FormAltaCarrera (forms.Form):
    OPCIONES_SELECCION = (
        (1, 'Diplomatura'),
        (2, 'Tecnicatura'),
        (3, 'Grado'),
        (4, 'Posgrado')    
    )
    carrera=forms.CharField(max_length=40, required=True)
    codigo=forms.CharField(max_length=20, required=True)
    tipo_carrera=forms.ChoiceField(
        required=True,
        choices=OPCIONES_SELECCION,
        widget= forms.RadioSelect()
    )
    plan_de_estudio=forms.IntegerField(required=True)
    resolucion_rectoral=forms.CharField(max_length=20, required=True)
    cantidad_asignaturas=forms.IntegerField(required=True)
    
class FormReporteCarrera (forms.Form):
    carrera=forms.CharField(required=True)

#COMISIONES
class FormAltaComisiones(forms.Form):
    OPCIONES_SELECCION1 = (
        ('Semi', 'Semipresencial'),
        ('Dist', 'Distancia'),
    )
    OPCIONES_SELECCION2 = (
        (15, '15 hs'),
        (19, '19 hs'),
    ) 
    OPCIONES_SELECCION3 = (
        ('COM-A', 'A'),
        ('COM-A', 'B'),
        ('COM-A', 'C'),
        ('COM-A', 'D'),
        ('COM-A', 'E'),
        ('COM-A', 'F'),   
    )     
    carrera=forms.CharField(max_length=40, required=True)
    asignatura=forms.CharField(max_length=20, required=True)
    codigo=forms.CharField(max_length=20, required=True)
    comision=forms.ChoiceField(
        required=True,
        choices=OPCIONES_SELECCION3,
        widget= forms.RadioSelect()
    )
    modalidad=forms.ChoiceField(
        required=True,
        choices=OPCIONES_SELECCION1,
        widget= forms.RadioSelect()
    )
    horario=forms.ChoiceField(
        required=True,
        choices=OPCIONES_SELECCION2,
        widget= forms.RadioSelect()
    )
    
class FormReporteComisiones(forms.Form):
    carrera=forms.CharField(required=True)