from django.db import models


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
         return "{} ({})" .format(self.nome, self.estado.nome)


    
# -----------------------------------------------------------------------------------------------------------

class Aluno(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Aluno")
    idade = models.IntegerField(verbose_name="Idade do Aluno")
    telefone = models.CharField(max_length=10, verbose_name="Telefone do Aluno")
    email = models.EmailField(verbose_name="Email do Aluno")

    def __str__(self):
          return f'{self.nome}'
    
    # -----------------------------------------------------------------------------------------------------------


    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Nome"