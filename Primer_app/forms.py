#importo forms de django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#CursoFormulario
class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


#ProfeFormulario

class ProfeFormulario(forms.Form):
    #especifico los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField()


class IntegrantesFormulario(forms.Form):

    #especifico los campos
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repetir la contraseña', widget= forms.PasswordInput)

    nombre = forms.CharField()
    apellido = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        #sacar los mensajes de ayuda
        help_texts = {k:""for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email ")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    

    class Meta:
        model = User
        fields = ['email','password1','password2']


class AvatarFormulario(forms.Form):
    img = forms.ImageField(required=True)
