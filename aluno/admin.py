from django.contrib import admin
from .models import Aluno, Categoria, Cidade, Estado, Exercicio, ExercicioTreino, Medida, Professor, Treino
# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Medida)
admin.site.register(Exercicio)
admin.site.register(ExercicioTreino)
admin.site.register(Treino)
admin.site.register(Categoria)