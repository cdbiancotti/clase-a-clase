from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from django.views.generic import CreateView, DetailView, DeleteView, ListView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate

from .forms import FormularioEstudiante, RegistroUsuarioForm, EditarUsuarioForm, AvatarForm

from .models import Avatar, Curso, Estudiante

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
            form.initial = {'username': None, 'password': None}
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


@login_required
def editar_user(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST)
        
        if form.is_valid():
            
            datos = form.cleaned_data
            
            usuario.email = datos['email']
            usuario.password1 = datos['password1']
            usuario.password2 = datos['password2']
            usuario.last_name = datos['last_name']
            usuario.first_name = datos['first_name']
            
            usuario.save()
            
            return render(request, 'Appcoder/index.html', {'tiene_mensaje': True, 'mensaje': f'Se edito correctamente.' })
    else:
        form = EditarUsuarioForm(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})
    
    return render(request, 'Appcoder/editar_user.html', {'form': form})

@login_required
def editar_avatar(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            # avatar = Avatar(user=usuario, avatar=form.cleaned_data['avatar'])
            
            avatar = Avatar.objects.get(user=usuario)
            avatar.avatar = form.cleaned_data['avatar']
            avatar.save()
            
            return render(request, 'Appcoder/index.html',
                          {'tiene_mensaje': True, 'mensaje': f'Se cargo correctamente el avatar.', 'url_avatar': avatar.avatar.url})
    else:
        form = AvatarForm()
    
    return render(request, 'Appcoder/editar_avatar.html', {'form': form})


def error_404(request, exception):
        data = {}
        return render(request,'Appcoder/login.html', data)