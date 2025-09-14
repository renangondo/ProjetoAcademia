from django.db import models

from medidas.models import Medida



# Create your models here.


class Estado(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome do Estado")
    sigla = models.CharField(max_length=2, verbose_name="Sigla do Estado")

    def __str__(self):
        return f'{self.nome} ({self.sigla})'

# -----------------------------------------------------------------------------------------------------------


class Cidade(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome da Cidade")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name="Estado")

    def __str__(self):
        return "{} ({})" .format(self.nome, self.estado)

# -----------------------------------------------------------------------------------------------------------

class Aluno(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Aluno")
    idade = models.IntegerField(verbose_name="Idade do Aluno")
    telefone = models.CharField(max_length=10, verbose_name="Telefone do Aluno")
    email = models.EmailField(verbose_name="Email do Aluno")
    objetivo = models.CharField(max_length=100, verbose_name="Objetivo do Aluno")
    status = models.BooleanField(default=True, verbose_name="Status do Aluno (Ativo/Inativo)")
    medidas = models.ForeignKey(Medida, on_delete=models.PROTECT, blank=True, verbose_name="Medidas do Aluno")
    login = models.CharField(max_length=20, verbose_name="Login do Aluno")
    senha = models.CharField(max_length=20, verbose_name="Senha do Aluno")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade do Aluno")

    def __str__(self):
        return f'{self.nome}'
# -----------------------------------------------------------------------------------------------------------

class Professor(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Professor")
    email = models.EmailField(verbose_name="Email do Professor")
    cpf = models.CharField(max_length=11, verbose_name="CPF do Professor")
    login = models.CharField(max_length=20, verbose_name="Login do Professor")
    senha = models.CharField(max_length=20, verbose_name="Senha do Professor")
    aluno = models.ManyToManyField(Aluno, on_delete=models.PROTECT, blank=True, verbose_name="Alunos do Professor")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade do Professor")

    def __str__(self):
        return f'{self.nome}'
# -----------------------------------------------------------------------------------------
