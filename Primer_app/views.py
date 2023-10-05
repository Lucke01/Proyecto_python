from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Primer_app.models import Curso,Profe,Integrantes


def inicio(request):
    return render(request, 'Primer_app/inicio.html')

def cursos(request):
    return render(request, 'Primer_app/Cursos.html')

def profes(request):

    return render(request, 'Primer_app/profes.html')

def integrantes(request):
    return render(request, 'Primer_app/integrantes.html')

def entregables(request):
    return render(request, 'Primer_app/entregables.html')

#---------------------------------------------------cursoFormulario-------------------------------------
from Primer_app.forms import CursoFormulario
def cursoFormulario(request):
    
    #creando formulario con DJANGO
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST) #hasta aca llega la info del html

        print(miFormulario)

        if miFormulario.is_valid(): #si paso la validacion de Django

            info = miFormulario.cleaned_data

            curso = Curso(nombre = info['curso'],comision = info['camada'])

            curso.save()

            return render(request,'Primer_app/Padre.html') #vuelvo a la pagina de inicio o donde quiero
        
    else: 

        miFormulario= CursoFormulario() #form vacio

    return render(request, "Primer_app/cursoFormulario.html", {"miFormulario":miFormulario})

#------------------------------profeFormulario-------------------------------------
from Primer_app.forms import ProfeFormulario
def profeFormulario(request):

    if request.method == 'POST':

        formprofe = ProfeFormulario(request.POST) #hasta aca llega la info del html

        print(formprofe)

        if formprofe.is_valid(): #si Django lo valida

            informacion = formprofe.cleaned_data

            profesor = Profe(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'],profesion = informacion['profesion'])

            profesor.save()

            return render(request,'Primer_app/Padre.html')#vuelvo a la pagina de inicio o donde quiero
        
    else: 

        formprofe = ProfeFormulario()#formulario vacio

    return render(request, "Primer_app/profeFormulario.html", {"formprofe":formprofe})



#---------------------------------------------IntegrantesFormulario-------------------------------------
from Primer_app.forms import IntegrantesFormulario

def integrantesFormulario(request):
    if request.method == 'POST':

        forminte = IntegrantesFormulario(request.POST) #hasta aca llega la info del html

        print(forminte)

        if forminte.is_valid(): #si Django lo valida

            infor = forminte.cleaned_data

            persona = Integrantes(nombre = infor['nombre'], apellido = infor['apellido'])

            persona.save()

            return render(request,'Primer_app/Padre.html') #vuelvo a la pagina de inicio o donde quiero
        
    else: 

        forminte = IntegrantesFormulario() #formulario vacio

    return render(request, "Primer_app/integrantesFormulario.html", {"forminte":forminte})


#-----------------------------------------------------busquedaComision------------------------
def busquedaComision(request):
    return render(request, "Primer_app/busquedaComision.html")

#------------------------------------------------------buscar----------------------------
def buscar(request):

    if request.GET['Comision']:

        comision = request.GET['Comision']
        cursos = Curso.objects.filter(comision__icontains = comision)
        
        return render(request, "Primer_app/resultadosBusqueda.html", {"cursos":cursos, 'Comision':comision})
    else:
        rta = "usted no cargo datos"
    return HttpResponse(rta)