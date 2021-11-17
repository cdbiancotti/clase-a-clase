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


def prueba_template(request):
    # template = loader.get_template('Appcoder/index.html')
    # documento = template.render({})
    # return HttpResponse(documento)
    return render(request, 'Appcoder/index.html', {})