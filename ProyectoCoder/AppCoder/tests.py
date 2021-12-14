from django.test import TestCase
from .models import Estudiante
# Create your tests here.

class EstudianteTest(TestCase):
    
    def setUp(self):
        Estudiante.objects.create(nombre='pepe', apellido='grillo')
        
    def test_existe_pepe(self):
        Estudiante.objects.get(nombre='pepe')