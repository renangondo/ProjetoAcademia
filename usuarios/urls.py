from django.urls import path
from django.contrib.auth import views as auth_views


from .views import EstadoCreate, CidadeCreate, AlunoCreate, ProfessorCreate
from .views import AlunoUpdate, CidadeUpdate, EstadoUpdate, ProfessorUpdate
from .views import EstadoDelete, CidadeDelete, AlunoDelete, ProfessorDelete
from .views import EstadoList, CidadeList, AlunoList, ProfessorList
from .views_usuario import AlunoUserCreate, ProfessorUserCreate

urlpatterns = [
    path('cadastrar/estado/', EstadoCreate.as_view(), name='cadastrar_estado'),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar_cidade'),
    path('cadastrar/aluno/', AlunoCreate.as_view(), name='cadastrar_aluno'),
    path('cadastrar/professor/', ProfessorCreate.as_view(), name='cadastrar_professor'),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar_estado'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar_cidade'),
    path('editar/aluno/<int:pk>/', AlunoUpdate.as_view(), name='editar_aluno'),
    path('editar/professor/<int:pk>/', ProfessorUpdate.as_view(), name='editar_professor'),

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name='excluir_estado'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir_cidade'),
    path('excluir/aluno/<int:pk>/', AlunoDelete.as_view(), name='excluir_aluno'),
    path('excluir/professor/<int:pk>/', ProfessorDelete.as_view(), name='excluir_professor'),

    path('listar/estado/', EstadoList.as_view(), name='listar_estado'),
    path('listar/cidade/', CidadeList.as_view(), name='listar_cidade'),
    path('listar/aluno/', AlunoList.as_view(), name='listar_alunos'),
    path('listar/professor/', ProfessorList.as_view(), name='listar_professor'),

    # URLs de registro de usuários
    path('registro/aluno/', AlunoUserCreate.as_view(), name='registro_aluno'),
    path('registro/professor/', ProfessorUserCreate.as_view(), name='registro_professor'),

    # urls de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='cadastros/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cadastros/login/logout.html'), name='logout'),
]