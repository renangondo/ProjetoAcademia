from django.contrib import admin

from treino.models import Categoria, Exercicio, Treino, ExercicioTreino

# Register your models here.

admin.site.register(Treino)
admin.site.register(Categoria)
admin.site.register(Exercicio)
admin.site.register(ExercicioTreino)
