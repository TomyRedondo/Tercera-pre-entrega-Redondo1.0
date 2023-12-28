from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso


def guardar_curso(request):
    curso = Curso(nombre="Programacion Avanzada", camada=7777)
    curso.save()
    
    return HttpResponse("El curso fue dado de alta")
