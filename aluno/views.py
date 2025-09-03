from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aluno, Professor, Medida, Exercicio, ExercicioTreino, Treino, Categoria, Cidade, Estado
from django.urls import reverse_lazy

class EstadoCreateView(CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html' 
    success_url = reverse_lazy('listar_estados')


class CidadeCreateView(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidades')

class MedidaCreateView(CreateView):
    model = Medida
    fields = ['altura', 'peso', 'cintura', 'quadril' , 'braco_direito', 'braco_esquerdo', 'coxa_direita', 'coxa_esquerda', 'panturrilha_direita', 'panturrilha_esquerda' , 'peito', 'largura_ombros']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_medidas')

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['nome', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_alunos')


class ProfessorCreateView(CreateView):
    model = Professor
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_professores')

class TreinoCreateView(CreateView):
    model = Treino
    fields = ['aluno', 'nome_treino', 'data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_treinos')

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_categorias')

class ExercicioCreateView(CreateView):
    model = Exercicio
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicios')

class ExercicioTreinoCreateView(CreateView):
    model = ExercicioTreino
    fields = ['treino', 'exercicio', 'series', 'repeticoes', 'descanso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicios_treino')
