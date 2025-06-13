from django.urls import path
from .views import AlunoView, AlunoCreateView

# path('endereço', minhaView.as_view(), name='nome_da_view')

urlpatterns = [
    path('', AlunoView.as_view(), name='aluno'), 
    path('cadastrar/aluno/', AlunoCreateView.as_view(), name = 'cadastrar-aluno')
]