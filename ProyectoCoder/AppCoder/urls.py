
from django.urls import path
from AppCoder.views import ver_curso, crear_curso, index, link1, link2, link3, link4

urlpatterns = [
    path('ver/', ver_curso, name='ver'),
    path('crear/', crear_curso, name='crear'),
    path('index/', index, name='index'),
    path('link1/', link1, name='link1'),
    path('link2/', link2, name='link2'),
    path('link3/', link3, name='link3'),
    path('link4/', link4, name='link4'),
]
