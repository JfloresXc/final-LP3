from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
layout = """"""
def integrantes(request):
    integrantes = ['Jose','Edson ','Miguel ']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def agregarCurso(request):
    return render(request, 'curso-agregar.html')

def carreras(request):
    return render(request, 'carreras.html')

def agregarCarrera(request):
    return render(request, 'carrera-agregar.html')




