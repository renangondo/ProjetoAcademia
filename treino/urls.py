from django.urls import path
from .views import (
    CategoriaCreate, CategoriaDelete, CategoriaUpdate, 
    ExercicioCreate, ExercicioDelete, ExercicioTreinoCreate, ExercicioTreinoDelete, ExercicioTreinoUpdate, 
    ExercicioUpdate, TreinoCreate, TreinoDelete, TreinoUpdate, TreinoList, TreinosAlunoList, TreinosProfessorList, 
    criar_treino_completo, DetalheTreinoView, TreinosDoAlunoView,
    # Adicione estas importações:
    exportar_treino_pdf, HistoricoTreinoList
)

# Importações das views de medidas para relatórios
from medidas.views import RelatorioProgressoView, exportar_relatorio_pdf

urlpatterns = [
    path('cadastrar/treino/', TreinoCreate.as_view(), name='cadastrar_treino'),
    path('atualizar/treino/<int:pk>/', TreinoUpdate.as_view(), name='atualizar_treino'),
    path('excluir/treino/<int:pk>/', TreinoDelete.as_view(), name='excluir_treino'),
    #################################################################################
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar_categoria'),
    path('atualizar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='atualizar_categoria'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir_categoria'),
    ##################################################################################
    path('cadastrar/exercicio/', ExercicioCreate.as_view(), name='cadastrar_exercicio'),
    path('atualizar/exercicio/<int:pk>/', ExercicioUpdate.as_view(), name='atualizar_exercicio'),
    path('excluir/exercicio/<int:pk>/', ExercicioDelete.as_view(), name='excluir_exercicio'),
    ##################################################################################
    path('cadastrar/ExercicioTreino/', ExercicioTreinoCreate.as_view(), name='cadastrar_treino_exercicio'),
    path('atualizar/ExercicioTreino/<int:pk>/', ExercicioTreinoUpdate.as_view(), name='atualizar_treino_exercicio'),
    path('excluir/ExercicioTreino/<int:pk>/', ExercicioTreinoDelete.as_view(), name='excluir_treino_exercicio'),
    path('listar/', TreinoList.as_view(), name='listar_treino'),
    path('meus-treinos/', TreinosAlunoList.as_view(), name='treinos_aluno'),
    path('treinos-professor/', TreinosProfessorList.as_view(), name='treinos_professor'),
    path('aluno/<int:aluno_id>/treinos/', TreinosDoAlunoView.as_view(), name='treinos_do_aluno'),
    path('aluno/<int:aluno_id>/novo-treino/', criar_treino_completo, name='criar_treino_completo'),
    path('treino/<int:pk>/detalhes/', DetalheTreinoView.as_view(), name='detalhes_treino'),
    ###################################################################################
    # Exportação PDF
    path('treino/<int:treino_id>/pdf/', exportar_treino_pdf, name='exportar_treino_pdf'),
    
    # Histórico
    path('treino/<int:treino_id>/historico/', HistoricoTreinoList.as_view(), name='historico_treino'),
    
    # Relatórios
    path('aluno/<int:aluno_id>/relatorio/', RelatorioProgressoView.as_view(), name='relatorio_progresso'),
    path('aluno/<int:aluno_id>/relatorio/pdf/', exportar_relatorio_pdf, name='exportar_relatorio_pdf'),
]
