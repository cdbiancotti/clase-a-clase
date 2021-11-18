from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Curso

# Create your views here.

def crear_curso(request):
    curso = Curso(nombre='After viejo', camada=25)
    curso.save()
    
    return HttpResponse(f'{curso.nombre} {curso.camada}')

def ver_curso(request):
    cursos = Curso.objects.all()[:5]
    curso1 = Curso.objects.get(nombre='Prueba2')
    
    texto = ''
    
    for curso in cursos:
        texto += f'Curso: {curso.nombre} <br>'
    
    return HttpResponse(f'{texto}')


def index(request):
    return render(request, 'Appcoder/index.html', {})

def link1(request):
    suma = 15 + 14
    return render(request, 'Appcoder/link1.html', {'suma': suma})

def link2(request):
    return render(request, 'Appcoder/link2.html', {})

def link3(request):
    return render(request, 'Appcoder/link3.html', {})

def link4(request):
    return render(request, 'Appcoder/link4.html', {})