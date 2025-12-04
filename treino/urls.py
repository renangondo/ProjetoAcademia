from django.urls import path
from .views import (
    CategoriaCreate, CategoriaDelete, CategoriaUpdate, CategoriaList,
    ExercicioCreate, ExercicioDelete, ExercicioTreinoCreate, ExercicioTreinoDelete, ExercicioTreinoUpdate, ExercicioTreinoList,
    ExercicioUpdate, ExercicioList, TreinoCreate, TreinoDelete, TreinoUpdate, TreinoList, TreinosAlunoList, TreinosProfessorList, 
    criar_treino_completo, DetalheTreinoView, TreinosDoAlunoView,
    exportar_treino_pdf, HistoricoTreinoList
)

# Importações das views de medidas para relatórios
from medidas.views import RelatorioProgressoView, exportar_relatorio_pdf

urlpatterns = [
    # URLs de Treino
    path('cadastrar/treino/', TreinoCreate.as_view(), name='cadastrar_treino'),
    path('editar/treino/<int:pk>/', TreinoUpdate.as_view(), name='editar_treino'),
    path('excluir/treino/<int:pk>/', TreinoDelete.as_view(), name='excluir_treino'),
    path('listar/treino/', TreinoList.as_view(), name='listar_treino'),
    
    # URLs de Categoria 
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar_categoria'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar_categoria'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir_categoria'),
    path('listar/categoria/', CategoriaList.as_view(), name='listar_categoria'),
    
    # URLs de Exercício 
    path('cadastrar/exercicio/', ExercicioCreate.as_view(), name='cadastrar_exercicio'),
    path('editar/exercicio/<int:pk>/', ExercicioUpdate.as_view(), name='editar_exercicio'),
    path('excluir/exercicio/<int:pk>/', ExercicioDelete.as_view(), name='excluir_exercicio'),
    path('listar/exercicio/', ExercicioList.as_view(), name='listar_exercicio'),
    
    # URLs de Exercício do Treino 
    path('cadastrar/exercicio-treino/', ExercicioTreinoCreate.as_view(), name='cadastrar_exercicio_treino'),
    path('editar/exercicio-treino/<int:pk>/', ExercicioTreinoUpdate.as_view(), name='editar_exercicio_treino'),
    path('excluir/exercicio-treino/<int:pk>/', ExercicioTreinoDelete.as_view(), name='excluir_exercicio_treino'),
    path('listar/exercicio-treino/', ExercicioTreinoList.as_view(), name='listar_exercicio_treino'),
    
    # URLs específicas de treino
    path('meus-treinos/', TreinosAlunoList.as_view(), name='treinos_aluno'),
    path('treinos-professor/', TreinosProfessorList.as_view(), name='treinos_professor'),
    path('aluno/<int:aluno_id>/treinos/', TreinosDoAlunoView.as_view(), name='treinos_do_aluno'),
    path('aluno/<int:aluno_id>/novo-treino/', criar_treino_completo, name='criar_treino_completo'),
    path('treino/<int:pk>/detalhes/', DetalheTreinoView.as_view(), name='detalhes_treino'),
    
    # URLs de funcionalidades extras
    path('treino/<int:treino_id>/pdf/', exportar_treino_pdf, name='exportar_treino_pdf'),
    path('treino/<int:treino_id>/historico/', HistoricoTreinoList.as_view(), name='historico_treino'),
    
    # URLs de relatórios
    path('aluno/<int:aluno_id>/relatorio/', RelatorioProgressoView.as_view(), name='relatorio_progresso'),
    path('aluno/<int:aluno_id>/relatorio/pdf/', exportar_relatorio_pdf, name='exportar_relatorio_pdf'),
]
