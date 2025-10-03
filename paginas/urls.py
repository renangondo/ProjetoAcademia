from django.urls import path
from .views import IndexView, AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView


# path('endereço', minhaView.as_view(), name='nome_da_view')

urlpatterns = [
    path('home/', IndexView.as_view(), name='index'),
    path('list/', AlunoListView.as_view(), name='aluno_list'),
    path('novo/', AlunoCreateView.as_view(), name='aluno_create'),
    path('editar/<int:pk>/', AlunoUpdateView.as_view(), name='aluno_edit'),
    path('excluir/<int:pk>/', AlunoDeleteView.as_view(), name='aluno_delete'),
]