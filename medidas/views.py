from django.shortcuts import render
from .models import Medidas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class MedidasCreate(CreateView):
    model = Medidas # modelo que irá ser cadastrado
    fields = ['aluno', 'data', 'peso', 'altura', 'peito', 'cintura', 'quadril', 'braco_direito', 'braco_esquerdo', 'coxa_direita', 'coxa_esquerda'] # campos do formulário, que serão exibidos
    template_name = 'cadastros/form.html'
    # Redireciona para a lista de alunos após o cadastro
    success_url = reverse_lazy('listar_alunos')

class MedidasUpdate(UpdateView):
    model = Medidas
    fields = ['aluno', 'data', 'peso', 'altura', 'peito', 'cintura', 'quadril', 'braco_direito', 'braco_esquerdo', 'coxa_direita', 'coxa_esquerda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_alunos')

class MedidasDelete(DeleteView):
    model = Medidas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_alunos')