from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.generic import CreateView, DetailView, DeleteView, ListView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate

from .forms import FormularioEstudiante, RegistroUsuarioForm

from .models import Curso, Estudiante

# Create your views here.

# def crear_estudiante(request, id):
    
#     # Manejado con un formulario propio
#     # if request.method == 'POST':
#     #     nombre = request.POST['nombre']
#     #     apellido = request.POST['apellido']
#     #     email = request.POST['email']
#     #     estudiante = Estudiante(nombre=nombre, apellido=apellido,email=email)
#     # else:
#     #     # curso = Curso(nombre='Repaso del after', camada=18)
#     #     estudiante = Estudiante(nombre='Pepe', apellido='Grillo',email='pepe.g@gmail.com')
#     #     # curso.save()
    
#     # estudiante.save()
#     # # return HttpResponse(f'{curso.nombre} {curso.camada}')
#     # # return HttpResponse(f'{estudiante.nombre} {estudiante.apellido}')
#     # return render(request, 'Appcoder/crear_curso.html', {'estudiante': estudiante})
    
#     # Manejado con un formulario basado en forms
    
#     # Manejado con un formulario propio
#     id_estudiante = 0
#     try:
#         estudiante = Estudiante.objects.get(id=id)
#         id_estudiante = estudiante.id
#     except Exception as e:
#         estudiante = None
    
#     if request.method == 'POST':
#         formulario = FormularioEstudiante(request.POST)
        
#         if formulario.is_valid():
#             datos_estudiante = formulario.cleaned_data
#             if estudiante:
#                 estudiante.nombre = datos_estudiante['nombre']
#                 estudiante.apellido = datos_estudiante['apellido']
#                 estudiante.email = datos_estudiante['email']
#             else:
#                 estudiante = Estudiante(nombre=datos_estudiante['nombre'], apellido=datos_estudiante['apellido'], email=datos_estudiante['email'])
            
#             estudiante.save()
#     elif estudiante:
#         formulario = FormularioEstudiante({'nombre': estudiante.nombre, 'apellido':estudiante.apellido, 'email':estudiante.email})
#     else:
#         formulario = FormularioEstudiante()
#     return render(request, 'Appcoder/crear_estudiante.html', {'estudiante': estudiante, 'formulario': formulario, 'idestudiante': id_estudiante})

# def ver_estudiantes(request):
    
#     # if request.method == 'GET':
#     # # estudiantes = Estudiante.objects.all()
#     #     apellido = request.GET.get('apellido', '')
#     #     estudiantes = Estudiante.objects.filter(apellido=apellido)
#     # # cursos = Curso.objects.all()[:5]
#     # # curso1 = Curso.objects.get(nombre='Prueba2')
#     # else:
#     estudiantes = Estudiante.objects.all()
        
#     # texto = ''
    
#     # for curso in cursos:
#     #     texto += f'Curso: {curso.nombre} <br>'
        
        
#     # for estudiante in estudiantes:
#     #     texto += f'Estudiante: {estudiante.nombre} {estudiante.apellido} <br>'
    
#     # return HttpResponse(f'{curso1.nombre} {curso1.camada}')
#     return render(request, 'AppCoder/ver_estudiante.html', {'estudiantes': estudiantes})

# def eliminar_estudiante(request, id):
#     estudiante = Estudiante.objects.get(id=id)
#     estudiante.delete()
#     return render(request, 'AppCoder/estudiante_eliminado.html', {'estudiante': estudiante})

def index(request):
    return render(request, 'Appcoder/index.html', {})

@login_required
def link1(request):
    suma = 15 + 14
    return render(request, 'Appcoder/link1.html', {'suma': suma})

def link2(request):
    return render(request, 'Appcoder/link2.html', {})

def link3(request):
    return render(request, 'Appcoder/link3.html', {})

def link4(request):
    return render(request, 'Appcoder/link4.html', {})

class EstudianteCreateView(CreateView):
    model = Estudiante
    success_url = 'AppCoder/estudiantes/lista'
    fields = ['nombre', 'apellido', 'email']
    template_name = "crear_estudiante.html"

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = 'AppCoder/estudiantes/lista'

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "detalle_estudiante.html"

class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "Appcoder/ver_estudiante.html"


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'Appcoder/index.html', {'tiene_mensaje': True, 'mensaje': 'Te logueaste con exito!'})
            else:
                return render(request, 'Appcoder/login.html', {'form': form, 'mensaje': 'Error, credenciales incorrectas.', 'error': True})
        
        else:
            return render(request, 'Appcoder/login.html', {'form': form, 'mensaje': 'Error, Los datos pasados tienen un mal formato.', 'error': True})
            
    
    form = AuthenticationForm
    
    return render(request, 'Appcoder/login.html', {'form': form, 'mensaje': '', 'error': False})


def register_request(request):
    
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            
            form.save()
            
            return render(request, 'Appcoder/index.html', {'tiene_mensaje': True, 'mensaje': f'Se creo el {username}' })
    
    form = RegistroUsuarioForm()
    
    return render(request, 'Appcoder/register.html', {'form': form, 'mensaje': '', 'error': False})