"""Clase17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import fecha_actual, otra_vista, saludo, saludo_a, saludo_otro, anio_nacimiento, probandoTemplate

urlpatterns = [
    path('', saludo),
    path('otra-vista/', otra_vista),
    path('fecha-actual/', fecha_actual),
    path('probandoTemplate/', probandoTemplate),  
    path('<str:nombre>/', saludo_a),
    path('saludo-a/<nombre>', saludo_a),
    # path('<numero>/<nombre>/', saludo_otro),
    path('anio-nacimiento/<int:edad>/', anio_nacimiento),
    path('admin/', admin.site.urls),
]
