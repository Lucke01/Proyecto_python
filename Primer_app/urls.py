from django.urls import path
from Primer_app import views


urlpatterns = [
    path('',views.inicio, name = "Inicio"), #este fue nuenstro primer view
    path('cursos',views.cursos, name="Cursos"),
    path('profes',views.profes, name = "Profes"),
    path('integrantes',views.integrantes, name = "Integrantes"),
    path('entregables',views.entregables, name = "Entregables"),
    path('cursoFormulario',views.cursoFormulario, name = "CursoFormulario"),
    path('profeFormulario',views.profeFormulario, name = "ProfeFormulario"),
    path('integrantesFormulario',views.integrantesFormulario, name = "IntegrantesFormulario"),
    path('busquedaComision',views.busquedaComision, name ="BusquedaComision"),
    path('buscar/',views.buscar),
]