from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from treino.models import Categoria, Exercicio, ExercicioTreino, Treino, HistoricoTreino
from django.shortcuts import get_object_or_404
from usuarios.models import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io


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
    fields = ['nome', 'categoria', 'descricao']
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

    def form_valid(self, form):
        # Salvar dados anteriores
        dados_anteriores = {
            'nome_treino': self.object.nome_treino,
            'data_inicio': str(self.object.data_inicio),
            'data_fim': str(self.object.data_fim) if self.object.data_fim else None,
            'descricao': self.object.descricao,
        }
        
        response = super().form_valid(form)
        
        # Salvar no histórico
        salvar_historico_treino(
            self.object,
            self.request.user,
            'edicao',
            f'Treino editado por {self.request.user.username}',
            dados_anteriores
        )
        
        messages.success(self.request, f'Treino "{self.object.nome_treino}" atualizado com sucesso!')
        return response

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
    fields = ['treino', 'exercicio', 'series', 'repeticoes', 'descanso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_exercicio_treino')
    group_required = ["Professor", "Administrador"]

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        messages.success(self.request, 'Exercício adicionado ao treino com sucesso!')
        return super().form_valid(form)

class ExercicioTreinoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = ExercicioTreino
    fields = ['treino', 'exercicio', 'series', 'repeticoes', 'descanso']
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

#--------------------------------------------------------------

class HistoricoTreinoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = HistoricoTreino
    template_name = 'cadastros/listas/historico_treino.html'
    context_object_name = 'historicos'
    group_required = ["Professor", "Administrador"]

    def get_queryset(self):
        treino_id = self.kwargs['treino_id']
        return HistoricoTreino.objects.filter(treino_id=treino_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        treino_id = self.kwargs['treino_id']
        context['treino'] = get_object_or_404(Treino, id=treino_id)
        return context

@login_required
def exportar_treino_pdf(request, treino_id):
    """Exporta treino para PDF"""
    treino = get_object_or_404(Treino, id=treino_id)
    exercicios = ExercicioTreino.objects.filter(treino=treino).select_related('exercicio', 'exercicio__categoria')
    
    # Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="treino_{treino.nome_treino}_{treino.aluno.nome}.pdf"'
    
    # Buffer para o PDF
    buffer = io.BytesIO()
    
    # Criar documento
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        alignment=1  # Centralizado
    )
    
    story.append(Paragraph(f"FICHA DE TREINO - {treino.nome_treino.upper()}", title_style))
    story.append(Spacer(1, 12))
    
    # Informações do aluno e treino
    info_data = [
        ['ALUNO:', treino.aluno.nome],
        ['IDADE:', f"{treino.aluno.idade} anos"],
        ['OBJETIVO:', treino.aluno.objetivo or "Não informado"],
        ['PERÍODO:', f"{treino.data_inicio.strftime('%d/%m/%Y')} até {treino.data_fim.strftime('%d/%m/%Y') if treino.data_fim else 'Em andamento'}"],
        ['PROFESSOR:', treino.cadastrado_por.first_name or treino.cadastrado_por.username],
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # Descrição do treino
    if treino.descricao:
        story.append(Paragraph(f"<b>DESCRIÇÃO:</b> {treino.descricao}", styles['Normal']))
        story.append(Spacer(1, 15))
    
    # Exercícios
    story.append(Paragraph("EXERCÍCIOS", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    # Tabela de exercícios
    exercicios_data = [['EXERCÍCIO', 'CATEGORIA', 'SÉRIES', 'REPETIÇÕES', 'DESCANSO']]
    
    for ex in exercicios:
        exercicios_data.append([
            ex.exercicio.nome,
            str(ex.exercicio.categoria),
            str(ex.series),
            str(ex.repeticoes),
            f"{ex.descanso}s" if ex.descanso else "Não def."
        ])
    
    exercicios_table = Table(exercicios_data, colWidths=[2.5*inch, 1.2*inch, 0.8*inch, 1*inch, 1*inch])
    exercicios_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(exercicios_table)
    
    # Observações finais
    story.append(Spacer(1, 30))
    story.append(Paragraph("OBSERVAÇÕES:", styles['Heading3']))
    story.append(Paragraph("• Execute os exercícios com técnica correta", styles['Normal']))
    story.append(Paragraph("• Respeite os tempos de descanso indicados", styles['Normal']))
    story.append(Paragraph("• Em caso de dor ou desconforto, pare imediatamente", styles['Normal']))
    story.append(Paragraph("• Mantenha hidratação adequada durante o treino", styles['Normal']))
    
    # Construir PDF
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response

def salvar_historico_treino(treino, user, tipo_alteracao, descricao, dados_anteriores=None):
    """Função auxiliar para salvar histórico"""
    ultima_versao = HistoricoTreino.objects.filter(treino=treino).first()
    nova_versao = ultima_versao.versao + 1 if ultima_versao else 1
    
    HistoricoTreino.objects.create(
        treino=treino,
        versao=nova_versao,
        alterado_por=user,
        tipo_alteracao=tipo_alteracao,
        descricao_alteracao=descricao,
        dados_anteriores=dados_anteriores
    )



