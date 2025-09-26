from django.shortcuts import render


class TreinoCreate(CreateView):
    model = Treino
    fields = ['aluno, data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar_treino')


class TreinoCreate(CreateView):
    model = Treino
    fields = ['aluno, data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar_treino')



    
     