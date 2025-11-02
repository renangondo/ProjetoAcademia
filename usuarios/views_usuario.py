from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Aluno, Professor
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import Group

class AlunoUserCreate(CreateView):
    model = Aluno
    fields = ['nome', 'idade', 'cpf', 'telefone', 'objetivo', 'cidade', 'sexo']
    template_name = 'cadastros/registro/registro_aluno.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        email = self.request.POST.get('email', '').strip()

        if User.objects.filter(username=cpf).exists():
            messages.error(self.request, 'Já existe um usuário com este CPF.')
            return self.form_invalid(form)

        # Criar usuário
        user = User.objects.create_user(
            username=cpf,
            email=email or '',
            password=cpf,
            is_active=False  # Aguarda ativação
        )

        # Salvar aluno
        aluno = form.save(commit=False)
        aluno.usuario = user
        aluno.save()

        # Adicionar ao grupo
        aluno_group = Group.objects.get(name='Aluno')
        user.groups.add(aluno_group)

        messages.success(self.request, 'Cadastro realizado! Aguarde a ativação.')
        return redirect(self.success_url)


class ProfessorUserCreate(CreateView):
    model = Professor
    fields = ['nome', 'cpf', 'cidade']
    template_name = 'cadastros/registro/registro_professor.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        email = self.request.POST.get('email', '').strip()

        if User.objects.filter(username=cpf).exists():
            messages.error(self.request, 'Já existe um usuário com este CPF.')
            return self.form_invalid(form)

        user = User.objects.create_user(
            username=cpf,
            email=email or '',
            password=cpf,
            is_active=False
        )

        professor = form.save(commit=False)
        professor.usuario = user
        professor.save()

        # Adicionar ao grupo
        professor_group = Group.objects.get(name='Professor')
        user.groups.add(professor_group)

        messages.success(self.request, 'Cadastro realizado! Aguarde a ativação.')
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




