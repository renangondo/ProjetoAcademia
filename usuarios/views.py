from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Estado, Cidade, Aluno, Professor
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.

class EstadoCreate(CreateView):
    model = Estado # modelo que irá ser cadastrado
    fields = ['nome', 'sigla'] # campos do formulário, que serão exibidos
    template_name = 'cadastros/form.html'
    # Redireciona para a lista de estados após o cadastro
    success_url = reverse_lazy('listar_estado')


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidade')
    
  


class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome', 'idade', 'telefone', 'email', 'objetivo', 'status', 'medidas', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_aluno')
    

class ProfessorCreate(CreateView):
    model = Professor
    fields = ['nome', 'email', 'cpf', 'login', 'senha', 'cidade']
    template_name = 'cadastros/form.html'
    
###################### UPDATE  ###########################################################################

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_estado')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidade')


class AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['nome', 'idade', 'telefone', 'email', 'objetivo', 'status', 'medidas', 'cidade']
    template_name = 'cadastros/form.html'


class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['nome', 'email', 'cpf', 'login', 'senha', 'cidade']
    template_name = 'cadastros/form.html'

###################### DELETE  ###########################################################################

class EstadoDelete(DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_estado')

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_cidade')

class AlunoDelete(DeleteView):
    model = Aluno
    template_name = 'cadastros/form-excluir.html'
    # success_url = '/'  # Redireciona para a página inicial após a exclusão

class ProfessorDelete(DeleteView):
    model = Professor
    template_name = 'cadastros/form-excluir.html'
    # success_url = '/'  # Redireciona para a página inicial após a exclusão

###################### LIST  ###########################################################################

class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/listas/estado.html'
    

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'

class AlunoList(ListView):
    model = Aluno
    template_name = 'cadastros/listas/aluno.html'

class ProfessorList(ListView):
    model = Professor
    template_name = 'cadastros/listas/professor.html'
