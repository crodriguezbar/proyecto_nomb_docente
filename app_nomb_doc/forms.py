from dataclasses import fields
from datetime import datetime
from django import forms
from app_nomb_doc.models import Carreras, Comisiones, Docentes, Asignaturas
from django.core.validators import RegexValidator

#Letras minusculas
class LetrasMinusculas(forms.CharField): #OK
    def to_python(self, value):
        return value.lower()

#FORMULARIOS DOCENTES
class FormAltaDocente (forms.ModelForm): #OK!!!

    #Validaciones
    nombre=forms.CharField( #OK
        label='NOMBRE',
        min_length=3, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidas!')],
        widget=forms.TextInput(attrs={'placeholder':'nombre'})
    )
    apellido=forms.CharField( #OK
        label='APELLIDO',
        min_length=3, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidas!')],
        widget=forms.TextInput(attrs={'placeholder':'apellido'})
    )
    fecha_nacimiento=forms.DateField(
        label='FECHA DE NACIMIENTO',
        widget=forms.DateInput(attrs={'style': 'cursor:pointer', 'type':"date", 'max':datetime.now().date()}),
    )  
    email=LetrasMinusculas( #OK
        label='DIRECCION DE EMAIL',
        min_length=8, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Ingrese una direccion valida de email!')],
        widget=forms.TextInput(attrs={'placeholder':'nombre@ejemplo.com'})
    )
    titulo_grado=forms.CharField( #OK
        label='TITULO DE GRADO',
        min_length=5, max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'titulo grado'})
    )
    titulo_posgrado=forms.CharField( #OK
        label='TITULO DE POSGRADO',
        max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'titulo posgrado'})
    ) 
    hs_asignar=forms.CharField( #OK
        label='HORAS A ASIGNAR',
        max_length=2,
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'horas a asignar'})
    )
    fecha_alta=forms.DateField(
        label='FECHA DE ALTA DOCENTE',
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
    )  
    
    class Meta: #OK
        model=Docentes #OK
        exclude=['fecha_creacion'] #OK
        labels={
            'dni':'DNI',
            'telefono':'TELEFONO',
            'metodo_alta':'METODO DE ALTA DOCENTE',
        }
        OPCIONES_METODO = (
            ('', 'Seleccione el metodo'),
            ('Seleccion docente', 'Seleccion docente'),
            ('Necesidad y urgencia', 'Necesidad y urgencia'),    
        )
        widgets={
            'dni': forms.TextInput(attrs={
                'style': 'font-size: 16px',
                'placeholder':'dni',
                'data-mask':'00.000.000'}),
            'metodo_alta': forms.Select(
                choices=OPCIONES_METODO,
                attrs={'class': 'form-control'
                }),
            'telefono': forms.TextInput(attrs={
                'style': 'font-size: 16px',
                'placeholder':'(012) 345-6789',
                'data-mask':'(000) 000-0000'})
        }
    #Super Funcion
    def __init__(self, *args, **kwargs):
        super(FormAltaDocente,self).__init__(*args, **kwargs)
        
        error_messages = ['nombre','apellido', 'dni', 'fecha_nacimiento', 'telefono','email', 'titulo_grado',
            'titulo_posgrado', 'hs_asignar','metodo_alta','fecha_alta'
        ]
        for field in error_messages:
            self.fields[field].error_messages.update({'required':'Este campo no puede estar vacio'})
        
class FormReporteDocente (forms.Form):
    desde_fecha_alta=forms.DateField(
        label='DESDE FECHA DE ALTA',
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
        required=False
    )
    hasta_fecha_alta=forms.DateField(
        label='HASTA FECHA DE ALTA',
        widget=forms.DateInput(attrs={'type':"date", 'max':datetime.now().date()}),
        required=False
    )
    dni=forms.CharField(
        label='DNI',
        widget=forms.TextInput(attrs={
                'style': 'font-size: 16px',
                'placeholder':'dni',
                'data-mask':'00.000.000'}),
        required=False
    )  
    
#FORMULARIOS CARRERAS
class FormAltaCarrera (forms.ModelForm):
    
    carrera=forms.CharField(
        label='CARRERA',
        max_length=40, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidas!')],
        widget=forms.TextInput(attrs={'placeholder':'nombre'})
    )
    plan_de_estudio=forms.CharField(
        label='PLAN DE ESTUDIO (AÑO)',
        max_length=4, 
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'año'})                           
    )
    resolucion_rectoral=forms.CharField(
        label='RESOLUCION RECTORAL DE APROBACION',
        max_length=20, 
        widget=forms.TextInput(attrs={'placeholder':'codigo'})
    )
    cantidad_asignaturas=forms.CharField(
        label='CANTIDAD TOTAL DE MATERIAS',
        max_length=2, 
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'cantidad'})
    )
    
    class Meta:
        model=Carreras
        fields='__all__'
        labels={
            'tipo_carrera':'TIPO DE CARRERA',
            'codigo':'CODIGO',
        }
        OPCIONES_TIPO_CARRERA=(
            ('', 'Seleccione un tipo'),
            ('Diplomatura', 'Diplomatura'),
            ('Tecnicatura', 'Tecnicatura'),
            ('Grado', 'Grado'),
            ('Posgrado', 'Posgrado')
        )
        widgets= {
            'tipo_carrera': forms.Select(
                choices=OPCIONES_TIPO_CARRERA,
                attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={
                'style': 'font-size: 16px',
                'placeholder':'iniciales carrera',
                'data-mask':'AA'}),        
        }
    def __init__(self, *args, **kwargs):
        super(FormAltaCarrera,self).__init__(*args, **kwargs)
        
        error_messages = ['carrera','plan_de_estudio', 'resolucion_rectoral', 'cantidad_asignaturas', 'tipo_carrera', 'codigo']
        for field in error_messages:
            self.fields[field].error_messages.update({'required':'Este campo no puede estar vacio'})

#Forms Alta Asignaturas
class FormCodigo(forms.ModelForm):
    class Meta:
        model=Asignaturas
        exclude = ('anio_semestre', 'asignatura')
        labels={
            'codigo':'CODIGO',
        }
        
class FormAnioSemestre(forms.ModelForm):
    anio_semestre=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
                'style': 'font-size: 16px',
                'placeholder':'año-semestre',
                'data-mask':'0-0'}),
        required=True
    )  
    class Meta:
        model=Asignaturas
        exclude = ('codigo','asignatura')

class FormAsignaturas(forms.ModelForm):
    asignatura=forms.CharField(
        label='',
        required=False,
        max_length=40, 
        widget=forms.TextInput(attrs={'placeholder':'asignatura'}),
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidos!')])
    class Meta:
        model=Asignaturas
        exclude = ('codigo','anio_semestre')

class FormReporteCarrera (forms.Form):
    carrera=forms.CharField(required=True)

class FormReporteAsignatura (forms.Form):
    codigo=forms.CharField(required=True)    
    

#COMISIONES
class FormAltaComisiones(forms.ModelForm):
    anio_academico=forms.CharField(
        max_length=4,
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        label='AÑO ACADEMICO',
        widget=forms.TextInput(attrs={'placeholder':'año academico'}),
        required=True
    )
    class Meta:
        model= Comisiones
        exclude=['fecha_creacion']
        labels={
            'codigo': 'CODIGO CARRERA',
            'asignatura': 'ASIGNATURA',
            'semestre_academico':'SEMESTRE ACADEMICO',
            'comision': 'COMISION',
            'modalidad': 'MODALIDAD',
            'horario': 'HORARIO',
        }
        OPCIONES_SEMESTRE = (
            ('', 'Seleccione semestre'),
            ('1° sem', '1° Semestre'),
            ('2° sem', '2° Semestre'),
        )
        OPCIONES_MODALIDAD = (
            ('', 'Seleccione modalidad'),
            ('Semi', 'Semipresencial'),
            ('Dist', 'Distancia'),
        )
        OPCIONES_HORARIO = (
            ('', 'Seleccione horario'),
            (15, '15 hs'),
            (19, '19 hs'),
        ) 
        OPCIONES_COMISION = (
            ('', 'Seleccione letra'),
            ('COM-A', 'A'),
            ('COM-B', 'B'),
            ('COM-C', 'C'),
            ('COM-D', 'D'),
            ('COM-E', 'E'),
            ('COM-F', 'F'),   
        )     
        widgets={
            'semestre_academico' : forms.Select(
                choices=OPCIONES_SEMESTRE,attrs={
                'class': 'form-control'}),
            'comision' : forms.Select(
                choices=OPCIONES_COMISION,attrs={
                'class': 'form-control'}),
            'modalidad' : forms.Select(
                choices=OPCIONES_MODALIDAD,attrs={
                'class': 'form-control'}),  
            'horario' : forms.Select(
                choices=OPCIONES_HORARIO,attrs={
                'class': 'form-control'}),    
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)               
        self.fields['asignatura'].queryset = Asignaturas.objects.none() #OK
        if 'codigo' in self.data:
            try: 
                codigo_id=int(self.data.get('codigo'))
                self.fields['asignatura'].queryset = Asignaturas.objects.filter(codigo_id=codigo_id).order_by('codigo')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['asignatura'].queryset = self.instance.codigo.asignatura_set.order_by('asignatura')

class FormReporteComisiones(forms.ModelForm): 
    codigo=forms.CharField(
        label='CARRERA',
        required=False,
        max_length=2, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Solo letras estan permitidas!')],
        widget=forms.TextInput(attrs={'placeholder':'carrera'})
    )
    anio_academico=forms.CharField(
        max_length=4,
        validators=[RegexValidator(r'^[0-9]*$', message='Solo numeros estan permitidos!')],
        widget=forms.TextInput(attrs={'placeholder':'año academico'}),
        label='AÑO ACADEMICO',
        required=False
    )
    

    class Meta:
        model= Comisiones
        exclude=['fecha_creacion', 'modalidad']
        labels={
            'codigo': 'CARRERA',
            'anio_academico': 'AÑO ACADEMICO',
            'semestre_academico':'SEMESTRE ACADEMICO',
        }
        OPCIONES_SEMESTRE = (
            ('', 'Seleccione semestre'),
            ('1° sem', '1° Semestre'),
            ('2° sem', '2° Semestre'),
        )
        widgets={
            'semestre_academico' : forms.Select(
                choices=OPCIONES_SEMESTRE,attrs={
                "required": True,
                'class': 'form-control',
                }),
        }
    