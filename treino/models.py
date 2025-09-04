from django.db import models

from usuarios.models import Aluno

# Create your models here.

class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    nome_treino = models.CharField(max_length=100, verbose_name="Nome do Treino")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim", null=True, blank=True)
    descricao = models.TextField(verbose_name="Descrição do Treino")

    def __str__(self):
        return f'{self.nome_treino} - {self.aluno}'
# ------------------------------------------------------------------------------    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")

    def __str__ (self):
        return self.nome

# -----------------------------------------------------------------------------------------------------------
class Exercicio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Exercício")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria do Exercício")
    descricao = models.TextField(verbose_name="Descrição do Exercício")

    def __str__(self):
        return self.nome
    
# -----------------------------------------------------------------------------------------------------------

class ExercicioTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, verbose_name="Treino")
    exercicio = models.ForeignKey(Exercicio, on_delete=models.PROTECT, verbose_name="Exercício")
    series = models.PositiveIntegerField(verbose_name="Número de Séries")
    repeticoes = models.PositiveIntegerField(verbose_name="Número de Repetições")

    def __str__(self):
        return f'{self.exercicio.nome} no treino {self.treino.nome_treino}'