from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse('Hola alumnos!')

def otra_vista(request):
    return HttpResponse('<h1>Otra vista</h1>')

def fecha_actual(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'<h1>{fecha_actual}</h1>')

def saludo_a(request, nombre):
    nombre_limpio = nombre.replace('-', ' ')
    return HttpResponse(f'Hola {nombre_limpio}!')

def saludo_otro(request, numero, nombre):
    nombre_limpio = nombre.replace('-', ' ')
    return HttpResponse(f'Hola {nombre_limpio}! ({numero})')

def anio_nacimiento(request, edad):
    anio_de_nacimimiento = datetime.now().year - edad
    return HttpResponse(f'{anio_de_nacimimiento}')

def probandoTemplate(self):
    # otra forma de render - otra forma de manejar archivo
    miHtml = open("C:\Source Code\Clase17\Clase17\plantillas\prueba.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)