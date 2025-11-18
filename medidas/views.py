from django.shortcuts import render, get_object_or_404
from .models import Medidas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from usuarios.models import Aluno
from treino.models import Treino

# Importações para gráficos e PDF
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Para usar sem interface gráfica
from io import BytesIO
import base64
import io

# Importações para PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Create your views here.

class MedidasCreate(LoginRequiredMixin, CreateView):
    model = Medidas
    fields = ['aluno', 'peso', 'altura', 'peito', 'cintura', 'quadril', 'braco_direito', 'braco_esquerdo', 'coxa_direita', 'coxa_esquerda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_medidas')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)

class MedidasUpdate(LoginRequiredMixin, UpdateView):
    model = Medidas
    fields = ['aluno', 'peso', 'altura', 'peito', 'cintura', 'quadril', 'braco_direito', 'braco_esquerdo', 'coxa_direita', 'coxa_esquerda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_medidas')

class MedidasDelete(LoginRequiredMixin, DeleteView):
    model = Medidas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_medidas')

class MedidasList(LoginRequiredMixin, ListView):
    model = Medidas
    template_name = 'cadastros/listas/medidas.html'
    context_object_name = 'medidas'

#-----------------------------------------------------------------------------------#

class RelatorioProgressoView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/progresso_aluno.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aluno_id = self.kwargs['aluno_id']
        aluno = get_object_or_404(Aluno, id=aluno_id)
        
        # Buscar medidas do aluno (corrigido nome do modelo)
        medidas = Medidas.objects.filter(aluno=aluno).order_by('data_medida')
        
        # Gerar gráficos
        graficos = {}
        
        if medidas.exists():
            # Gráfico de Peso
            graficos['peso'] = self.gerar_grafico_peso(medidas)
            
            # Gráfico de IMC
            graficos['imc'] = self.gerar_grafico_imc(medidas)
            
            # Estatísticas
            context['estatisticas'] = {
                'total_medidas': medidas.count(),
                'primeira_medida': medidas.first().data_medida,
                'ultima_medida': medidas.last().data_medida,
                'peso_inicial': medidas.first().peso,
                'peso_atual': medidas.last().peso,
                'diferenca_peso': medidas.last().peso - medidas.first().peso,
                'imc_atual': self.calcular_imc(medidas.last().peso, medidas.last().altura),
            }
        
        context.update({
            'aluno': aluno,
            'medidas': medidas,
            'graficos': graficos,
            'treinos_count': Treino.objects.filter(aluno=aluno).count(),
        })
        
        return context
    
    def gerar_grafico_peso(self, medidas):
        """Gera gráfico de evolução do peso"""
        plt.figure(figsize=(10, 6))
        datas = [m.data_medida for m in medidas]
        pesos = [m.peso for m in medidas]
        
        plt.plot(datas, pesos, marker='o', linewidth=2, markersize=6)
        plt.title('Evolução do Peso', fontsize=16, fontweight='bold')
        plt.xlabel('Data')
        plt.ylabel('Peso (kg)')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # Converter para base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', dpi=300)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        
        plt.close()
        return graphic
    
    def gerar_grafico_imc(self, medidas):
        """Gera gráfico de evolução do IMC"""
        plt.figure(figsize=(10, 6))
        datas = [m.data_medida for m in medidas]
        imcs = [self.calcular_imc(m.peso, m.altura) for m in medidas]
        
        plt.plot(datas, imcs, marker='s', linewidth=2, markersize=6, color='orange')
        plt.title('Evolução do IMC', fontsize=16, fontweight='bold')
        plt.xlabel('Data')
        plt.ylabel('IMC')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # Linhas de referência IMC
        plt.axhline(y=18.5, color='blue', linestyle='--', alpha=0.7, label='Abaixo do peso')
        plt.axhline(y=25, color='green', linestyle='--', alpha=0.7, label='Peso normal')
        plt.axhline(y=30, color='red', linestyle='--', alpha=0.7, label='Obesidade')
        plt.legend()
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', dpi=300)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        
        plt.close()
        return graphic
    
    def calcular_imc(self, peso, altura):
        """Calcula o IMC"""
        if altura > 0:
            return peso / (altura * altura)
        return 0

@login_required
def exportar_relatorio_pdf(request, aluno_id):
    """Exporta relatório de progresso em PDF"""
    aluno = get_object_or_404(Aluno, id=aluno_id)
    medidas = Medidas.objects.filter(aluno=aluno).order_by('data_medida')  # Corrigido nome do modelo
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="relatorio_progresso_{aluno.nome}.pdf"'
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Título
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=20, spaceAfter=30, alignment=1)
    story.append(Paragraph(f"RELATÓRIO DE PROGRESSO - {aluno.nome.upper()}", title_style))
    
    # Informações do aluno
    info_data = [
        ['ALUNO:', aluno.nome],
        ['IDADE:', f"{aluno.idade} anos"],
        ['OBJETIVO:', aluno.objetivo or "Não informado"],
        ['TOTAL DE MEDIDAS:', str(medidas.count())],
    ]
    
    if medidas.exists():
        info_data.extend([
            ['PRIMEIRA MEDIDA:', medidas.first().data_medida.strftime('%d/%m/%Y')],
            ['ÚLTIMA MEDIDA:', medidas.last().data_medida.strftime('%d/%m/%Y')],
            ['PESO INICIAL:', f"{medidas.first().peso} kg"],
            ['PESO ATUAL:', f"{medidas.last().peso} kg"],
            ['DIFERENÇA:', f"{medidas.last().peso - medidas.first().peso:+.1f} kg"],
        ])
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # Tabela de medidas
    if medidas.exists():
        story.append(Paragraph("HISTÓRICO DE MEDIDAS", styles['Heading2']))
        
        medidas_data = [['DATA', 'PESO (kg)', 'ALTURA (m)', 'IMC']]
        
        for medida in medidas:
            imc = medida.peso / (medida.altura * medida.altura) if medida.altura > 0 else 0
            medidas_data.append([
                medida.data_medida.strftime('%d/%m/%Y'),
                str(medida.peso),
                str(medida.altura),
                f"{imc:.1f}"
            ])
        
        medidas_table = Table(medidas_data)
        medidas_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(medidas_table)
    
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response

