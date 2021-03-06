
from django import template
from django.urls import path

from AppCoder.views import index, link1, link2, link3, link4, login_request, register_request, editar_user, editar_avatar

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    # path('ver/', ver_estudiantes, name='ver'),
    # path('crear/<int:id>', crear_estudiante, name='crear'),
    # path('eliminar/<int:id>', eliminar_estudiante, name='eliminar'),
    path('index/', index, name='index'),
    path('link1/', link1, name='link1'),
    path('link2/', link2, name='link2'),
    path('link3/', link3, name='link3'),
    path('link4/', link4, name='link4'),
    path('estudiantes/lista', views.EstudianteListView.as_view(), name='List'),
    path('crear/', views.EstudianteCreateView.as_view(), name='Create'),
    path('eliminar/<int:id>', views.EstudianteDeleteView.as_view(), name='Delete'),
    path('detalle/<int:id>', views.EstudianteDetailView.as_view(), name='Detail'),
    path('login/', login_request, name='Login'),
    path('register/', register_request, name='Register'),
    path('editar/', editar_user, name='Editar'),
    path('editar-avatar/', editar_avatar, name='Editar_Avatar'),
    path('logout/', LogoutView.as_view(template_name='Appcoder/logout.html'), name='Logout'),
]
