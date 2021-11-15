from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

# Create your views here.

def crear_curso(request):
    curso = Curso(nombre='After nuevo', camada=25)
    curso.save()
    
    return HttpResponse(f'{curso.nombre} {curso.camada}')

def ver_curso(request):
    cursos = Curso.objects.all()[:5]
    curso1 = Curso.objects.get(nombre='Prueba2')
    
    texto = ''
    
    for curso in cursos:
        texto += f'Curso: {curso.nombre} <br>'
    
    return HttpResponse(f'{curso1}')