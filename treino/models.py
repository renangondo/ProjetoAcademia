from django.db import models

from usuarios.models import Aluno

# Create your models here.

class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    nome_treino = models.CharField(max_length=100, verbose_name="Nome do Treino")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim", null=True, blank=True)
    descricao = models.TextField(verbose_name="Descrição do Treino")

    cadastrado_em = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")
    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name="Cadastrado por", related_name='treinos_principais_cadastrados')


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
    descanso = models.IntegerField(verbose_name="Descanso entre as séries")

    cadastrado_em = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")
    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name="Cadastrado por", related_name='exercicios_treinos_cadastrados')

    def __str__(self):
        return f'{self.exercicio.nome} no treino {self.treino.nome_treino}'
    

