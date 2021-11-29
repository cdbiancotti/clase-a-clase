from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'Camada: {self.camada} - {self.nombre}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    profesion = models.CharField(max_length=20)

class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.DateField()
    entregado = models.BooleanField()