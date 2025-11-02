from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Estado, Cidade, Aluno
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin 
from braces.views import GroupRequiredMixin

# Create your views here.

class EstadoCreate(CreateView):
    model = Estado # modelo que irá ser cadastrado
    fields = ['nome', 'sigla'] # campos do formulário, que serão exibidos
    template_name = 'cadastros/form.html'
    # Redireciona para a lista de estados após o cadastro
    success_url = reverse_lazy('listar_estado')


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['id','nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidade')
    
  
class AlunoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Aluno
    fields = ['nome', 'idade', 'cpf', 'telefone', 'objetivo', 'cidade', 'status', 'sexo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_aluno')
    group_required = ["Professor", "Administrador"]

    def form_valid(self, form):
        try:
            # Criação de um usuário para o aluno aonde o nome de usuário e a senha serão o CPF sem máscaras
            import re
            cpf_clean = re.sub(r'\D', '', form.instance.cpf)  # Remove qualquer caractere
            usuario = User.objects.create_user(username=cpf_clean, password=cpf_clean)
        except Exception:
            form.add_error('cpf', 'Erro ao criar usuário. Verifique se o CPF já está cadastrado.')
            return self.form_invalid(form)

        form.instance.usuario = usuario
        form.instance.professor = self.request.user

        response = super().form_valid(form)
        # Mensagem de sucesso para aparecer na lista de alunos
        messages.success(self.request, f'Aluno "{self.object.nome}" criado com sucesso.')

        return response
    
###################### UPDATE  ###########################################################################

class EstadoUpdate(LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_estado')


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidade')


class AlunoUpdate(LoginRequiredMixin, UpdateView):
    model = Aluno
    fields = ['nome', 'cpf','idade', 'telefone', 'objetivo', 'cidade', 'status', 'professor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_alunos')


###################### DELETE  ###########################################################################

class EstadoDelete(LoginRequiredMixin, DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_estado')

class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_cidade')

class AlunoDelete(LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_alunos')

###################### LIST  ###########################################################################

class EstadoList(LoginRequiredMixin, ListView):
    model = Estado
    template_name = 'cadastros/listas/estado.html'
    

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'

class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'cadastros/listas/aluno.html'

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Aluno.objects.none()
        if user.is_superuser:
            return Aluno.objects.all()
        return Aluno.objects.filter(professor=user)
