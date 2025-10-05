from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aluno

# ListView - Exibe a lista de alunos
class IndexView(TemplateView):
    template_name = 'paginas/index.html'



class LandingPageView(TemplateView):
    template_name = 'paginas/landing_page.html'








# class AlunoListView(ListView):
#    model = Aluno
#    template_name = 'paginas/formularioTemplate.html'
#    context_object_name = 'alunos'

# CreateView - Cria um novo aluno


#class AlunoCreateView(CreateView):
#    model = Aluno
#    template_name = 'paginas/cadastroTemplate.html'
#    fields = ['nome', 'treino', 'status']
#    success_url = reverse_lazy('index')

# UpdateView - Atualiza os dados de um aluno


#class AlunoUpdateView(UpdateView):
#    model = Aluno
#    template_name = 'paginas/cadastroTemplate.html'
#    fields = ['nome', 'treino', 'status']
#    success_url = reverse_lazy('aluno_list')

# DeleteView - Exclui um aluno


#class AlunoDeleteView(DeleteView):
#    model = Aluno
#    template_name = ''
#    success_url = reverse_lazy('')

