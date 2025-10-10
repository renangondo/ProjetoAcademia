from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Estado, Cidade, Aluno
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.

class EstadoCreate(CreateView):
    model = Estado # modelo que irá ser cadastrado
    fields = ['nome', 'sigla'] # campos do formulário, que serão exibidos
    template_name = 'cadastros/form.html'
    # Redireciona para a lista de estados após o cadastro
    success_url = reverse_lazy('listar_estado')


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidade')
    
  
class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome','cpf' , 'idade', 'telefone',  'objetivo', 'cidade', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_alunos')

    def form_valid(self, form):

        try: 
            # Criação de um usuário para o aluno aonde o nome de usuário  a senha será o CPF sem mascaras
            import re
            cpf_clean = re.sub(r'\D', '', form.instance.cpf)  # Remove qualquer caractere
            usuario = User.objects.create_user(username=cpf_clean, password=cpf_clean)
        except:
            form.add_error('cpf', 'Erro ao criar usuário. Verifique se o CPF já está cadastrado.')
            return self.form_invalid(form)

        form.instance.usuario = usuario
        form.instance.professor = self.request.user

        url =  super().form_valid(form)

        return url
    
###################### UPDATE  ###########################################################################

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_estado')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_cidade')


class AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['nome', 'cpf','idade', 'telefone', 'objetivo', 'cidade', 'status', 'professor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar_alunos')


###################### DELETE  ###########################################################################

class EstadoDelete(DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_estado')

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_cidade')

class AlunoDelete(DeleteView):
    model = Aluno
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar_alunos')

###################### LIST  ###########################################################################

class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/listas/estado.html'
    

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'

class AlunoList(ListView):
    model = Aluno
    template_name = 'cadastros/listas/aluno.html'

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Aluno.objects.none()
        if user.is_superuser:
            return Aluno.objects.all()
        return Aluno.objects.filter(professor=user)
