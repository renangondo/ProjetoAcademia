from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from treino.models import Categoria, Exercicio, ExercicioTreino, Treino
from django.shortcuts import get_object_or_404
from usuarios.models import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
# ========================= CATEGORIA VIEWS =========================
class CategoriaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_categoria')
    group_required = ["Professor", "Administrador"]

class CategoriaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_categoria')
    group_required = ["Professor", "Administrador"]

class CategoriaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_categoria')
    group_required = ["Professor", "Administrador"]

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

# ========================= EXERCICIO VIEWS =========================
class ExercicioCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Exercicio
    fields = ['nome', 'categoria', 'descricao', 'descanso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio')
    group_required = ["Professor", "Administrador"]

class ExercicioUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Exercicio
    fields = ['nome', 'categoria', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio')
    group_required = ["Professor", "Administrador"]

class ExercicioDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Exercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_exercicio')
    group_required = ["Professor", "Administrador"]

class ExercicioList(LoginRequiredMixin, ListView):
    model = Exercicio
    template_name = 'cadastros/listas/exercicio.html'

# ========================= TREINO VIEWS =========================
class TreinoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Treino
    fields = ['aluno', 'nome_treino', 'data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_treino')
    group_required = ["Professor", "Administrador"]

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        messages.success(self.request, f'Treino "{form.instance.nome_treino}" criado com sucesso!')
        return super().form_valid(form)

class TreinoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Treino
    fields = ['aluno', 'nome_treino', 'data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_treino')
    group_required = ["Professor", "Administrador"]

class TreinoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Treino
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_treino')
    group_required = ["Professor", "Administrador"]

class TreinoList(LoginRequiredMixin, ListView):
    model = Treino
    template_name = 'cadastros/listas/treino.html'
    context_object_name = 'treinos'

# ========================= TREINO VIEWS ESPECÍFICAS =========================
class TreinosAlunoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Treino
    template_name = 'cadastros/listas/treino_aluno.html'
    context_object_name = 'treinos'
    group_required = ["Aluno", "Professor", "Administrador"]
    
    def get_queryset(self):
        try:
            # Assumindo que o usuário tem uma relação OneToOne com Aluno
            aluno = self.request.user.aluno
            return Treino.objects.filter(aluno=aluno)
        except:
            return Treino.objects.none()

class TreinosProfessorList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Treino
    template_name = 'cadastros/listas/treino_professor.html'
    context_object_name = 'treinos'
    group_required = ["Professor"]
    
    def get_queryset(self):
        return Treino.objects.filter(cadastrado_por=self.request.user)

# ========================= EXERCICIO TREINO VIEWS =========================
class ExercicioTreinoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = ExercicioTreino
    fields = ['treino', 'exercicio', 'series', 'repeticoes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio_treino')
    group_required = ["Professor", "Administrador"]

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        messages.success(self.request, 'Exercício adicionado ao treino com sucesso!')
        return super().form_valid(form)

class ExercicioTreinoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = ExercicioTreino
    fields = ['treino', 'exercicio', 'series', 'repeticoes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio_treino')
    group_required = ["Professor", "Administrador"]

class ExercicioTreinoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = ExercicioTreino
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_exercicio_treino')
    group_required = ["Professor", "Administrador"]

class ExercicioTreinoList(LoginRequiredMixin, ListView):
    model = ExercicioTreino
    template_name = 'cadastros/listas/exercicio_treino.html'
    context_object_name = 'exercicios_treino'

@login_required
def criar_treino_completo(request, aluno_id):
    """View para criar treino e adicionar exercícios"""
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        # Dados do treino principal
        nome_treino = request.POST.get('nome_treino')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        descricao = request.POST.get('descricao')
        
        # Criar o treino principal
        treino = Treino.objects.create(
            aluno=aluno,
            nome_treino=nome_treino,
            data_inicio=data_inicio,
            data_fim=data_fim if data_fim else None,
            descricao=descricao,
            cadastrado_por=request.user
        )
        
        # Processar exercícios
        exercicios_ids = request.POST.getlist('exercicio')
        series_list = request.POST.getlist('series')
        repeticoes_list = request.POST.getlist('repeticoes')
        descanso_list = request.POST.getlist('descanso')
        
        # Criar ExercicioTreino para cada exercício
        for i in range(len(exercicios_ids)):
            if exercicios_ids[i]:  # Se exercício foi selecionado
                ExercicioTreino.objects.create(
                    treino=treino,
                    exercicio_id=exercicios_ids[i],
                    series=int(series_list[i]) if i < len(series_list) else 1,
                    repeticoes=int(repeticoes_list[i]) if i < len(repeticoes_list) else 1,
                    descanso=int(descanso_list[i]) if i < len(descanso_list) and descanso_list[i] else None,
                    cadastrado_por=request.user
                )
        
        messages.success(request, f'Treino "{nome_treino}" criado com sucesso!')
        return redirect('treinos_do_aluno', aluno_id=aluno.id)
    
    # GET - Mostrar formulário
    exercicios = Exercicio.objects.all().select_related('categoria')
    context = {
        'aluno': aluno,
        'exercicios': exercicios,
    }
    return render(request, 'cadastros/treino_completo.html', context)

class DetalheTreinoView(LoginRequiredMixin, DetailView):
    model = Treino
    template_name = 'cadastros/detalhe_treino.html'
    context_object_name = 'treino'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercicios_treino'] = ExercicioTreino.objects.filter(treino=self.object).select_related('exercicio', 'exercicio__categoria')
        return context

# Esta view você já tinha, só melhorei um pouco:
class TreinosDoAlunoView(LoginRequiredMixin, ListView):
    model = Treino
    template_name = 'cadastros/listas/treinos_do_aluno.html'
    context_object_name = 'treinos'
    
    def get_queryset(self):
        aluno_id = self.kwargs['aluno_id']
        return Treino.objects.filter(aluno_id=aluno_id).order_by('-cadastrado_em')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aluno_id = self.kwargs['aluno_id']
        context['aluno'] = get_object_or_404(Aluno, id=aluno_id)
        return context








