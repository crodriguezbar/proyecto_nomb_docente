from django.db import models

# Create your models here. Class CamelCase 

class Docentes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    titulo_grado=models.CharField(max_length=40)
    titulo_posgrado=models.CharField(max_length=40)
    hs_asignar=models.IntegerField()
    metodo_alta=models.CharField(max_length=100)
    fecha_alta=models.DateField()
    
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