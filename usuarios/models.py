from django.db import models
from django.utils import timezone



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



class Professor(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Professor")
    cpf = models.CharField(max_length=11, verbose_name="CPF do Professor")
    telefone = models.CharField(max_length=11, verbose_name="Telefone do Cliente")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade do Professor")

    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name="Usuário do Professor", related_name='professores_cadastrados')

    def __str__(self):
        return f'{self.nome}'
# -----------------------------------------------------------------------------------------

class Aluno(models.Model):

    SEXO = [('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')]
    STATUS = [('Ativo', 'Ativo'),('Inativo', 'Inativo'),('Pendente', 'Pendente'),
]

    nome = models.CharField(max_length=120, verbose_name="Nome do Aluno")
    idade = models.IntegerField(verbose_name="Idade do Aluno")
    cpf = models.CharField(max_length=11, verbose_name="CPF do Aluno", unique=True)
    telefone = models.CharField(max_length=10, verbose_name="Telefone do Aluno")
    objetivo = models.CharField(max_length=400, verbose_name="Objetivo do Aluno")
    data_criacao = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    status = models.CharField(max_length=12,choices=STATUS,default='Ativo')
    sexo = models.CharField(max_length=10, verbose_name="Sexo do Aluno", choices=SEXO, default='Outros')
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade do Aluno")

    professor = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name="Professor do Aluno", related_name='meus_alunos')
    usuario = models.OneToOneField('auth.User', on_delete=models.PROTECT, verbose_name="Usuário do Aluno", related_name='perfi_aluno')

    def __str__(self):
        return f'{self.nome}'
# -----------------------------------------------------------------------------------------------------------



