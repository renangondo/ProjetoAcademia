from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Aluno, Professor
from django.shortcuts import redirect
from django.contrib import messages

class AlunoUserCreate(CreateView):
    model = Aluno
    fields = ['nome', 'idade', 'cpf', 'telefone', 'objetivo', 'cidade', 'status', 'sexo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Cria um usuário com CPF como username
        cpf = form.cleaned_data['cpf']
        email = self.request.POST.get('email')  # Campo adicional do template
        senha = cpf  # Usando CPF como senha inicial

        # Verifica se já existe um usuário com esse CPF
        if User.objects.filter(username=cpf).exists():
            messages.error(self.request, 'Já existe um usuário com este CPF')
            return self.form_invalid(form)

        # Cria o usuário (inativo por padrão)
        user = User.objects.create_user(
            username=cpf,
            email=email,
            password=senha,
            is_active=False
        )

        # Salva o aluno vinculado ao usuário
        aluno = form.save(commit=False)
        aluno.usuario = user
        aluno.save()

        messages.success(self.request, 'Cadastro realizado com sucesso! Aguarde a ativação do seu usuário.')
        return redirect(self.success_url)

class ProfessorUserCreate(CreateView):
    model = Professor
    fields = ['nome', 'cpf', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Cria um usuário com CPF como username
        cpf = form.cleaned_data['cpf']
        email = self.request.POST.get('email')  # Campo adicional do template
        senha = cpf  # Usando CPF como senha inicial

        # Verifica se já existe um usuário com esse CPF
        if User.objects.filter(username=cpf).exists():
            messages.error(self.request, 'Já existe um usuário com este CPF')
            return self.form_invalid(form)

        # Cria o usuário (inativo por padrão)
        user = User.objects.create_user(
            username=cpf,
            email=email,
            password=senha,
            is_active=False
        )

        # Salva o professor vinculado ao usuário
        professor = form.save(commit=False)
        professor.usuario = user
        professor.save()

        messages.success(self.request, 'Cadastro realizado com sucesso! Aguarde a ativação do seu usuário.')
        return redirect(self.success_url)

###################### UPDATE  ###########################################################################

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['nome', 'cpf', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')





###################### DELETE  ###########################################################################

class ProfessorDelete(DeleteView):
    model = Professor
    template_name = 'cadastros/confirm_delete.html'
    success_url = reverse_lazy('listar_professor')


###################### LIST  ###########################################################################

class ProfessorList(ListView):
    model = Professor
    template_name = 'cadastros/listas/professor.html'




