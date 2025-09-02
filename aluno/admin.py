from django.contrib import admin
from .models import Aluno, Cidade, Estado
# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Aluno)