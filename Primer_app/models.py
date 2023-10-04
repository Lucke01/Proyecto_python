from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()


class Integrantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Profe (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


class Entregable (models.Model):
    nombre =models.CharField(max_length=30)
    entrega = models.DateField()
    entregado = models.BooleanField()