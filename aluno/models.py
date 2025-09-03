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
class Medida(models.Model):
     altura = models.FloatField(verbose_name="Altura do Aluno (m)")
     peso = models.FloatField(verbose_name="Peso do Aluno (kg)")
     cintura = models.FloatField(verbose_name="Cintura do Aluno (cm)")
     quadril = models.FloatField(verbose_name="Quadril do Aluno (cm)")
     braco_direito = models.FloatField(verbose_name="Braço Direito do Aluno (cm)")
     braco_esquerdo = models.FloatField(verbose_name="Braço Esquerdo do Aluno (cm)")
     coxa_direita = models.FloatField(verbose_name="Coxa Direita do Aluno (cm)")
     coxa_esquerda = models.FloatField(verbose_name="Coxa Esquerda do Aluno (cm)")
     panturrilha_direita = models.FloatField(verbose_name="Panturrilha Direita do Aluno (cm)")
     panturrilha_esquerda = models.FloatField(verbose_name="Panturrilha Esquerda do Aluno (cm)")
     peito = models.FloatField(verbose_name="Peito do Aluno (cm)")
     largura_ombros = models.FloatField(verbose_name="Largura dos Ombros do Aluno (cm)")

     def __str__(self):
          return f'{self.altura} - {self.peso} - {self.cintura} - {self.quadril} - {self.braco_direito} - {self.braco_esquerdo} - {self.coxa_direita} - {self.coxa_esquerda} - {self.panturrilha_direita} - {self.panturrilha_esquerda} - {self.peito} - {self.largura_ombros}'

# -----------------------------------------------------------------------------------------------------------
class Aluno(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Aluno")
    idade = models.IntegerField(verbose_name="Idade do Aluno")
    telefone = models.CharField(max_length=10, verbose_name="Telefone do Aluno")
    email = models.EmailField(verbose_name="Email do Aluno")
    objetivo = models.CharField(max_length=100, verbose_name="Objetivo do Aluno")
    status = models.BooleanField(default=True, verbose_name="Status do Aluno (Ativo/Inativo)")

    def __str__(self):
          return f'{self.nome}'
# -----------------------------------------------------------------------------------------------------------

class Professor(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Professor")
    email = models.EmailField(verbose_name="Email do Professor")
    cpf = models.CharField(max_length=11, verbose_name="CPF do Professor")
    login = models.CharField(max_length=20, verbose_name="Login do Professor")
    senha = models.CharField(max_length=20, verbose_name="Senha do Professor")

    def __str__(self):
          return f'{self.nome}'
# -----------------------------------------------------------------------------------------------------------

class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    nome_treino = models.CharField(max_length=100, verbose_name="Nome do Treino")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim", null=True, blank=True)
    descricao = models.TextField(verbose_name="Descrição do Treino")

    def __str__(self):
        return f'{self.nome_treino} - {self.aluno.nome}'

# -----------------------------------------------------------------------------------------------------------
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")

    def __str__(self):
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
    series = models.IntegerField(verbose_name="Número de Séries")
    repeticoes = models.IntegerField(verbose_name="Número de Repetições")
    descanso = models.DurationField(verbose_name="Tempo de Descanso")

    def __str__(self):
        return f'{self.treino.nome_treino} - {self.exercicio.nome}'

# -----------------------------------------------------------------------------------------------------------
