from django.urls import reverse, resolve
from django.test import TestCase
from app_nomb_doc.forms import FormAltaCarrera, FormAltaDocente
from app_nomb_doc.models import Docentes
from app_nomb_doc.views import alta_docente

# Create your tests here.

class DocentesTesT(TestCase):
    def setUp(self):
        Docentes.objects.create(
            nombre='claudio andres',
            apellido= 'Rodriguez barragan',
            titulo_grado='licenciatura en logistica',
            titulo_posgrado='ninguno',
            dni='11.111.111',
            fecha_nacimiento='2011-11-11',
            telefono='(132) 111-2222',
            email= 'FEFWEF@dwa.wd.com',
            hs_asignar='343',
            metodo_alta='Necesidad y urgencia',
            fecha_alta='2022-11-11',
        )

    def test_clean (self):
        docente1=Docentes.objects.get(dni='11.111.111')
        self.assertEqual(docente1.nombre, 'claudio andres')
        self.assertEqual(docente1.email, 'FEFWEF@dwa.wd.com')
        
class FormulariosTest(TestCase):
    
    def test_formulario_Alta_Docente(self):
        form=FormAltaDocente(data={
            'nombre':'claudio andres',
            'apellido':'Rodriguez barragan',
            'titulo_grado':'licenciatura en logistica',
            'titulo_posgrado':'ninguno',
            'dni':'11.111.111',
            'fecha_nacimiento':'2011-11-11',
            'telefono':'(132) 111-2222',
            'email': 'FEFWEF@dwa.wd.com',
            'hs_asignar':'343',
            'metodo_alta':'Necesidad y urgencia',
            'fecha_alta':'2022-11-11',
        })
        self.assertTrue(form.is_valid())
    
    
    def test_formulario_Alta_Carrera(self):
        form=FormAltaCarrera(data={
            'carrera':'Licenciatura en Logistica',
            'plan_de_estudio': 'xx',
            'resolucion_rectoral':'rr11',
            'cantidad_asignaturas':'345',
            'tipo_carrera':'Diplomatura',
            'codigo':'ll'
        })
        self.assertTrue(form.is_valid())

class ViewTest(TestCase):
    def test_url_alta_docente(self):
        url = reverse('altadocente')
        self.assertEquals(resolve(url).func, alta_docente)
        