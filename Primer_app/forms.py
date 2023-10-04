#importo forms de django

from django import forms
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