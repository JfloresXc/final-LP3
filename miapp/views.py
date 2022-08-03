from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from miapp.models import Course
from django.contrib import messages

# from .forms import CourseForm
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
    cursos = Course.objects.raw('SELECT * FROM miapp_course')
    return render(request, 'cursos.html', {'cursos': cursos})

def formularioCurso(request):
    return render(request, 'curso-agregar.html')

def agregarCurso(request):
    codigo = request.GET['codigo']
    nombre = request.GET['nombre']
    horas = request.GET['horas']
    creditos = request.GET['creditos']
    estado = request.GET['estado']

    course = Course(
        code = codigo,
        name = nombre,
        hour = horas,
        credits = creditos,
        state = estado
    )
    course.save()
    messages.add_message(request, messages.SUCCESS, "Curso agregado con éxito")

    return redirect('/agregarcurso/')

def carreras(request):
    return render(request, 'carreras.html')

def agregarCarrera(request):
    return render(request, 'carrera-agregar.html')




