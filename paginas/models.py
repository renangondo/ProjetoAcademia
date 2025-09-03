from django.db import models

# Create your models here.
 
STATUS = [
    ('Completo', 'Completo'),
    ('Pendente', 'Pendente'),
    ('Em Andamento', 'Em Andamento'),
]


class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    treino = models.CharField(max_length=80)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=12,
        choices=STATUS,
        default='Pendente', 
    )
    

    def __str__(self):
         return f'{self.nome} ({self.treino} - {self.data} - {self.status})'
    
    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "Aluno"