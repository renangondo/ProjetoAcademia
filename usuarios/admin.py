from django.contrib import admin

from usuarios.models import Aluno, Cidade, Estado, Professor

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Estado)
admin.site.register(Cidade)
