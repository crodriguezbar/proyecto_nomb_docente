from dataclasses import fields
from datetime import datetime
from django import forms
from app_nomb_doc.models import Docentes
from django.core.validators import RegexValidator

#FORMULARIOS DOCENTES
class FormAltaDocente (forms.ModelForm):
    OPCIONES_SELECCION = (
        ('Seleccion Docente', 'Seleccion Docente'),
        ('Necesidad y Urgencia', 'Necesidad y Urgencia'),    
    )
    #VALIDACIONES
    nombre=forms.CharField(
        label='NOMBRE',
        min_length=3, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidas!')],
        widget=forms.TextInput(attrs={'placeholder':'nombre'})
    )
    apellido=forms.CharField(
        label='APELLIDO',
        min_length=3, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidas!')],
        widget=forms.TextInput(attrs={'placeholder':'apellido'})
    )
    dni=forms.CharField(
        label='DNI',
        max_length=7, 
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'dni'})
    )
    fecha_nacimiento=forms.DateField(
        label='FECHA DE NACIMIENTO',
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
    )  
    titulo_grado=forms.CharField(
        label='TITULO DE GRADO',
        min_length=5, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'titulo grado'})
    )
    titulo_posgrado=forms.CharField(
        label='TITULO DE POSGRADO',
        min_length=5, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'titulo posgrado'})
    )
    hs_asignar=forms.IntegerField(
        label='HORAS A ASIGNAR',
        max_value=45,
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'horas a asignar'})
    )
    metodo_alta=forms.ChoiceField(
        label='METODO DE ALTA DOCENTE',
        required=True,
        choices=OPCIONES_SELECCION,
        widget= forms.RadioSelect()
    )
    fecha_alta=forms.DateField(
        label='FECHA DE ALTA DOCENTE',
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
    )  
    class Meta:
        model=Docentes
        exclude=['fecha_creacion']

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
        ('Diplomatura', 'Diplomatura'),
        ('Tecnicatura', 'Tecnicatura'),
        ('Grado', 'Grado'),
        ('Posgrado', 'Posgrado')    
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
        ('COM-B', 'B'),
        ('COM-C', 'C'),
        ('COM-D', 'D'),
        ('COM-E', 'E'),
        ('COM-F', 'F'),   
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