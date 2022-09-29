from django.db import models

# Create your models here. Class CamelCase 

class Docentes(models.Model):
    nombre=models.CharField(max_length=40) #OK
    apellido=models.CharField(max_length=40) #OK
    dni=models.CharField(max_length=10, unique=True) #OK
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=20) #OK
    email=models.EmailField(max_length=50, unique=True) #OK
    titulo_grado=models.CharField(max_length=40) #OK
    titulo_posgrado=models.CharField(max_length=40) #OK
    hs_asignar=models.CharField(max_length=2) #OK
    metodo_alta=models.CharField(max_length=40)
    fecha_alta=models.DateField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    
    # Primera letra mayuscula
    def clean(self):
        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title() 
        self.titulo_grado = self.titulo_grado.capitalize()
        self.titulo_posgrado = self.titulo_posgrado.capitalize()
     
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} DNI: {self.dni} Alta: {self.fecha_alta}'
    
    class Meta: #Para personalizar datos en admin
        verbose_name="Docente"
        verbose_name_plural="Docentes"
        db_table="Docentes"
    
class Carreras(models.Model):   #OK
    carrera=models.CharField(max_length=40)
    codigo=models.CharField(max_length=20, unique=True)
    tipo_carrera=models.CharField(max_length=40)
    plan_de_estudio=models.IntegerField()
    resolucion_rectoral=models.CharField(max_length=20) 
    cantidad_asignaturas=models.IntegerField()
    
    def clean(self):
        self.carrera = self.carrera.capitalize()
    
    class Meta: #Para personalizar datos en admin
        verbose_name="Carrera"
        verbose_name_plural="Carreras"
        db_table="Carreras"

class Asignaturas (models.Model):
    anio_semestre=models.CharField(max_length=40)
    asignatura=models.CharField(max_length=40)
    codigo=models.ForeignKey(Carreras, null=True, blank=True, on_delete=models.CASCADE) #establezco la relacion entre los modelos
    
    def clean(self):
        self.asignatura1 = self.asignatura1.title()
        self.asignatura2 = self.asignatura2.title()
        self.asignatura3 = self.asignatura3.title()
        self.asignatura4 = self.asignatura4.title()
        self.asignatura5 = self.asignatura5.title()
    
    class Meta: #Para personalizar datos en admin
        verbose_name="Asignatura"
        verbose_name_plural="Asignaturas"
        db_table="Asignaturas"


class Comisiones(models.Model):
    anio_academico=models.CharField(max_length=40, verbose_name="Año")#verbose hace que se muestre la denominacion que deseeo en admin
    semestre_academico=models.CharField(max_length=40, verbose_name="Semestre")
    comision=models.CharField(max_length=40, verbose_name="Comision")
    modalidad=models.CharField(max_length=40, verbose_name="Modalidad")
    horario=models.CharField(max_length=40, verbose_name="Horario")
    fecha_creacion=models.DateField(auto_now_add=True)
    codigo=models.ForeignKey(Carreras, null=True, blank=True, on_delete=models.CASCADE)
    asignatura=models.ForeignKey(Asignaturas, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta: #Para personalizar datos en admin
        verbose_name="Comision"
        verbose_name_plural="Comisiones"
        db_table="Comisiones"




