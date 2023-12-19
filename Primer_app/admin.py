from django.contrib import admin

from .models import *  #importamos models
# Register your models here.

admin.site.register(Curso)
admin.site.register(Integrantes)
admin.site.register(Profe)
admin.site.register(Entregable)
admin.site.register(Avatar)

