from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from treino.models import Categoria, Exercicio, ExercicioTreino, Treino


class TreinoCreate(CreateView):
    model = Treino
    fields = ['aluno', 'data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_treino')

    # Já Indentifica o usuário que está criando o treino
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class TreinoUpdate(UpdateView):
    model = Treino
    fields = ['aluno', 'data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_treino')

class TreinoDelete(DeleteView):
    model = Treino
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_treino')

#################################################################################

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_categoria')

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_categoria')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_categoria')

##################################################################################

class ExercicioCreate(CreateView):
    model = Exercicio
    fields = ['nome', 'categoria', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio')


class ExercicioUpdate(UpdateView):
    model = Exercicio
    fields = ['nome', 'categoria', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio') 

class ExercicioDelete(DeleteView):
    model = Exercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_exercicio')

###################################################################################

class ExercicioTreinoCreate(CreateView):
    model = ExercicioTreino
    fields = ['treino', 'exercicio', 'series', 'repeticoes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exerciciotreino')

    # Já Indentifica o usuário que está criando o treino
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)

class ExercicioTreinoUpdate(UpdateView):
    model = ExercicioTreino
    fields = ['treino', 'exercicio', 'series', 'repeticoes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exerciciotreino')

class ExercicioTreinoDelete(DeleteView):
    model = ExercicioTreino
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_exerciciotreino')

    





    
     