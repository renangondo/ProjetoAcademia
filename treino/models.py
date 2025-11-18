from django.db import models
from django.contrib.auth.models import User
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
    
    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"
# ------------------------------------------------------------------------------    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")

    def __str__ (self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

# -----------------------------------------------------------------------------------------------------------
class Exercicio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Exercício")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria do Exercício")
    descricao = models.TextField(verbose_name="Descrição do Exercício")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"
    
# -----------------------------------------------------------------------------------------------------------

class ExercicioTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, verbose_name="Treino")
    exercicio = models.ForeignKey(Exercicio, on_delete=models.PROTECT, verbose_name="Exercício")
    series = models.PositiveIntegerField(verbose_name="Número de Séries")
    repeticoes = models.PositiveIntegerField(verbose_name="Número de Repetições")
    descanso = models.IntegerField(verbose_name="Descanso entre as séries", null=True, blank=True)

    cadastrado_em = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")
    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name="Cadastrado por", related_name='exercicios_treinos_cadastrados')

    def __str__(self):
        return f'{self.exercicio.nome} no treino {self.treino.nome_treino}'
    
    class Meta:
        verbose_name = "Exercício do Treino"
        verbose_name_plural = "Exercícios dos Treinos"
# -----------------------------------------------------------------------------------------------------------
class HistoricoTreino(models.Model):
   treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='historico')
   versao = models.PositiveIntegerField(default=1)
   data_alteracao = models.DateTimeField(auto_now_add=True)
   alterado_por = models.ForeignKey(User, on_delete=models.CASCADE)
   tipo_alteracao = models.CharField(max_length=50, choices=[
        ('criacao', 'Criação'),
        ('edicao', 'Edição'),
        ('exercicio_add', 'Exercício Adicionado'),
        ('exercicio_rem', 'Exercício Removido'),
        ('exercicio_edit', 'Exercício Editado'),
    ])
   descricao_alteracao = models.TextField()
   dados_anteriores = models.JSONField(null=True, blank=True)  # Armazena dados da versão anterior

   class Meta:
        ordering = ['-data_alteracao']
        verbose_name = 'Histórico de Treino'
        verbose_name_plural = 'Históricos de Treinos'
    
   def __str__(self):
        return f"{self.treino.nome_treino} - v{self.versao} - {self.tipo_alteracao}"




