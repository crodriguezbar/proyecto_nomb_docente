from django.db import models

# Create your models here. Class CamelCase 

class Docentes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.CharField(max_length=7)
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    titulo_grado=models.CharField(max_length=40)
    titulo_posgrado=models.CharField(max_length=40)
    hs_asignar=models.CharField(max_length=2)
    metodo_alta=models.CharField(max_length=40)
    fecha_alta=models.DateField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    
    # Primera letra mayuscula
    def clean(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize() 
        self.titulo_grado = self.titulo_grado.capitalize()
        self.titulo_posgrado = self.titulo_posgrado.capitalize()
        
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} DNI: {self.dni} Alta: {self.fecha_alta}'
    
class Carreras(models.Model):   
    carrera=models.CharField(max_length=40)
    codigo=models.CharField(max_length=20)
    tipo_carrera=models.CharField(max_length=40)
    plan_de_estudio=models.IntegerField()
    resolucion_rectoral=models.CharField(max_length=20) 
    cantidad_asignaturas=models.IntegerField()
    asignaturas=models.CharField(max_length=40)
    
class Comisiones(models.Model):
    carrera=models.CharField(max_length=40)
    asignatura=models.CharField(max_length=40)
    codigo=models.CharField(max_length=40)
    comision=models.CharField(max_length=40)
    modalidad=models.CharField(max_length=40)
    horario=models.CharField(max_length=40)