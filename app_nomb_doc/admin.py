from django.contrib import admin
from .models import *
# Register your models here. para que impacte en BD

@admin.register(Docentes)
class AdminDocentes(admin.ModelAdmin):
    list_display=(
        'id', 
        'nombre', 
        'apellido', 
        'dni', 
        'hs_asignar',
        'fecha_alta',
    )
    ordering = ('-fecha_alta',)
    search_fields= ('dni', 'apellido', 'hs_asignar')
    list_display_links = ('dni', 'apellido', 'hs_asignar')
    list_filter = ('hs_asignar',)
    list_per_page = 10
    
@admin.register(Carreras)
class AdminCarreras(admin.ModelAdmin):
    list_display=(
        'id', 
        'carrera', 
        'plan_de_estudio', 
        'tipo_carrera', 
        'codigo', 
        'cantidad_asignaturas',
    )
    search_fields= ('carrera', 'plan_de_estudio', 'tipo_carrera')
    list_display_links = ('carrera', 'plan_de_estudio')
    list_filter = ('carrera', 'plan_de_estudio')
    list_per_page = 10
    
@admin.register(Asignaturas)
class AdminAsignaturas(admin.ModelAdmin):
    list_display=(
        'id', 
        'anio_semestre', 
        'asignatura', 
        
    )
    search_fields= ('anio_semestre', 'asignatura')
    list_display_links = ('anio_semestre',)
    list_filter = ('anio_semestre',)
    list_per_page = 10