from django.urls import path
from Primer_app import views


urlpatterns = [
    path('',views.inicio),
    path('cursos',views.cursos, name="Cursos"),
    path('profes',views.profe),
    path('integrantes',views.integrantes),
    path('entregable',views.entregables),
]