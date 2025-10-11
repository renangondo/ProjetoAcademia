from django.urls import path
from .views import CategoriaCreate, CategoriaDelete, CategoriaUpdate, ExercicioCreate, ExercicioDelete, ExercicioTreinoCreate, ExercicioTreinoDelete, ExercicioTreinoUpdate, ExercicioUpdate, TreinoCreate, TreinoDelete, TreinoUpdate
from .views import treinos_do_aluno


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
    path('aluno/<int:aluno_id>/treinos/', treinos_do_aluno, name='treinos_do_aluno'),
]
