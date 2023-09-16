from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Primer_app.models import Curso

def inicio(request):
    return render(request, 'Primer_app/inicio.html')

def cursos(request):
    return render(request, 'Primer_app/Curso.html')

def profe(request):
    return render(request, 'Primer_app/profes.html')

def integrantes(request):
    return render(request, 'Primer_app/integrantes.html')

def entregables(request):
    return render(request, 'Primer_app/entregables.html')
