from django.db import models


# Create your models here.
class Medidas(models.Model):

    altura = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Altura (m)")
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    cintura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cintura (cm)")
    quadril = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Quadril (cm)")
    braco_direito = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Braço Direito (cm)")
    braco_esquerdo = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Braço Esquerdo (cm)")
    coxa_direita = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Coxa Direita (cm)")
    coxa_esquerda = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Coxa Esquerda (cm)")
    panturrilha_direita = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Panturrilha Direita (cm)")
    panturrilha_esquerda = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Panturrilha Esquerda (cm)")
    peito = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peito (cm)")
    largura_ombros = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Largura dos Ombros (cm)")
    data_medida = models.DateField(auto_now_add=True, verbose_name="Data da Medida")

    def __str__(self):
        return f'Data de {self.data_medida}'