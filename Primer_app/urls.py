from django.urls import path
from Primer_app import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',views.inicio, name = "Inicio"), #este fue nuenstro primer view
    path('cursos',views.cursos, name="Cursos"),
    path('profes',views.profes, name = "Profes"),
    path('integrantes',views.integrantes, name = "Integrantes"),
    path('entregables',views.entregables, name = "Entregables"),
    #path('cursoFormulario',views.cursoFormulario, name = "CursoFormulario"),
    #path('profeFormulario',views.profeFormulario, name = "ProfeFormulario"),
    #path('integrantesFormulario',views.integrantesFormulario, name = "IntegrantesFormulario"),
    path('busquedaComision',views.busquedaComision, name ="BusquedaComision"),
    path('buscar/',views.buscar),

    #--------------------------Crud de Model Profesor
    path('leerProfesores',views.leerProfesores, name = "LeerProfesores"),
    path('eliminarProfesor/<profesorNombre>/',views.eliminarProfesor, name = "EliminarProfesor"),
    path('editarProfesor/<profesorNombre>/',views.editarProfesor, name = "EditarProfesor"),

    #---------------------Crud model Integrantes
    path('leer_integrantes',views.leer_integrantes, name = "LeerIntegrantes"),
    path('eliminar_integrante/<nombreIntegrante>/',views.eliminar_integrantes, name = "EliminarIntegrante"),
    path('editar_integrante/<nombreIntegrante>/',views.editar_integrantes,name='EditarIntegrante'),

    #--------------------login--------------------------------------------------------------------
    path('login',views.login_request, name = 'Login'),

    #------------------register-----------------------------------------------------------------------
    path('register',views.register, name = "Register"),

    #---------------------logout
    path('logout',LogoutView.as_view(template_name='Primer_app/logout.html'),name = "LogOut"),

    #--------------------EdicionPerfil

    path('editarPerfil',views.editarPerfil, name = "EditarPerfil"),

    #------------------Agregaravatar

    path('agregarAvatar',views.agregar_avatar, name ="AgregarAvatar"),
  
 

    
]


