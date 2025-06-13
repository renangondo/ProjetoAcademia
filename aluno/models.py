from django.db import models

# Create your models here.
class Aluno(models.Model): 
    nome = models.CharField(max_length=120)
    idade = models.IntegerField(),
    telefone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
          return f'{self.nome}'


    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Nome"