from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Primer_app.models import Curso,Profe,Integrantes
from Primer_app.forms import CursoFormulario,ProfeFormulario,IntegrantesFormulario,UserRegisterForm




#-----------------------------------------------------inicio.html-------------------------------------
def inicio(request):
    return render(request, 'Primer_app/inicio.html')

#---------------------------------------------------cursos.html//Formulario-------------------------------------

def cursos(request):
    
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

    return render(request, "Primer_app/cursos.html", {"miFormulario":miFormulario})

#------------------------------profes.html//Formulario-------------------------------------
def profes(request):

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

    return render(request, "Primer_app/profes.html", {"formprofe":formprofe})



#---------------------------------------------Integrantes.html//Formulario-------------------------------------
def integrantes(request):
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

    return render(request, "Primer_app/integrantes.html", {"forminte":forminte})


#-----------------------------------------------------busquedaComision------------------------
def busquedaComision(request):
    return render(request, "Primer_app/busquedaComision.html")

#------------------------------------------------------buscar----------------------------
def buscar(request):

    if request.GET['Comision']:

        comision = request.GET['Comision']
        cursos = Curso.objects.filter(comision__icontains = comision)
        
        return render(request, "Primer_app/inicio.html", {"cursos":cursos, 'Comision':comision})
    else:
        rta = "usted no cargo datos"
    #return HttpResponse(rta)
    return render(request, 'Primer_app/inicio.html',{"rta":rta})

#------------------------------------------------entregables.html----------------------------
def entregables(request):
    return render(request, 'Primer_app/entregables.html')



#-----------------------------------------------CRUD---------------------------

#---------------------------------------------leerProfesores.html----------------
def leerProfesores(request):
    profesores = Profe.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "Primer_app/leerProfesores.html",contexto)


#----------------------------------------------------Eliminarprofesor-------------------------------
def eliminarProfesor(request,profesorNombre):
    profesor = Profe.objects.get(nombre = profesorNombre)
    profesor.delete()
        
    #vuelvo al menu
    profesores = Profe.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "Primer_app/leerProfesores.html",contexto)   

#-------------------------------------------------------Editarprofesor--------------------------------
 
def editarProfesor(request, profesorNombre):      
    profesor = Profe.objects.get(nombre = profesorNombre)
    if request.method == "POST":
        formProfe = ProfeFormulario(request.POST)
        print(formProfe)

        if formProfe.is_valid():
            informacion = formProfe.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            return render(request, 'Primer_app/Padre.html',{"formProfe":formProfe})
    
    else:
        formProfe = ProfeFormulario(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,'email':profesor.email,'profesion':profesor.profesion})
       
    return render(request, 'Primer_app/editarProfesor.html',{"formProfe":formProfe,"profesorNombre":profesorNombre})




#-----------------------------------------Leer-Integrantes---------------------------------

def leer_integrantes(request):
    integrantes = Integrantes.objects.all()
    contexto = {"integrantes":integrantes}
    return render (request, "Primer_app/leer_integrantes.html",contexto)

#----------------------------eliminar-Integrantes---------------------------------
def eliminar_integrantes(request,nombreIntegrante):
    integrante = Integrantes.objects.get(nombre = nombreIntegrante)
    integrante.delete()

    #volver al menu
    integrantes = Integrantes.objects.all()
    context = {'integrantes':integrantes}
    return render(request,'Primer_app/leer_integrantes.html',context)

#---------------------------------Editar-Integrantes
def editar_integrantes(request,nombreIntegrante):       
    integrante = Integrantes.objects.get(nombre = nombreIntegrante)
    #accedo al formulario de integrantes
    if request.method == "POST":
        form_Inte= IntegrantesFormulario(request.POST)
        print(form_Inte)

        if form_Inte.is_valid():
            info = form_Inte.cleaned_data

            integrante.nombre = info['nombre']
            integrante.apellido = info['apellido']
            integrante.save()

        return render(request,'Primer_app/Padre.html',{"form_Inte":form_Inte})
        
    else:
        form_Inte = IntegrantesFormulario(initial={'nombre':integrante.nombre, 'apellido':integrante.apellido})
        
    return render(request,'Primer_app/editar_integrante.html',{"form_Inte":form_Inte,"nombreIntegrante":nombreIntegrante})
        
    



#------------------------------------------LOGIN--------------------------------------------------------------------------   
from django.contrib.auth.forms import AuthenticationForm as AF
from django.contrib.auth import login , logout, authenticate
def login_request(request):

    if request.method == "POST":    
        form = AF(request, data = request.post)

        #creo un if sobre el form
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username = usuario, pasword = contraseña) #autenticar si coincide el usuario

            # creo un if sobre user
            if user is not None:
                login(request,user)
                return render(request, 'Primer_app/inicio.html',{"mensaje":f"bienvenido {usuario}" })
        
            else:
                return render(request, 'Primer_app/inicio.html', {"mensaje":"Error, DATOS INCORRECTOS"})
    
        else:
            return render(request, 'Primer_app/inicio.html',{"mensaje":"ERROR, FORMULARIO ERRONEO"})

    form = AF()

    return render(request,"Primer_app/login.html", {"form":form})

#---------------------------------------REGISTER---------------------------------------------



def register(request):
    
    if request.method == "POST":
            #form = UCF(request.POST)
            form = UserRegisterForm(request.POST)

            if form.is_valid():
            
                username = form.cleaned_data['username']
                form.save()
                return render(request, "Primer_app/inicio.html", {"mensaje":"El usuario ha sido creado"},)
    else:
        #form = UCF()
        form = UserRegisterForm()
    
    return render(request,"Primer_app/registro.html", {"form":form})


#----------------------------------------DECORADORES----------------
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, "Primer_app/inicio.html")

    

#AGREGAR CRUD AL LOGIN


   
  
        
   
