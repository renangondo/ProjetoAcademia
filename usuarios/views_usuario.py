from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Aluno, Professor
from django.shortcuts import redirect
from django.contrib import messages

class AlunoUserCreate(CreateView):
    model = Aluno
    fields = ['nome', 'idade', 'cpf', 'telefone', 'objetivo', 'cidade', 'status', 'sexo']
    template_name = 'cadastros/registro/registro_aluno.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        email = self.request.POST.get('email', '').strip()

        if User.objects.filter(username=cpf).exists():
            messages.error(self.request, 'Já existe um usuário com este CPF.')
            return self.form_invalid(form)

        user = User.objects.create_user(username=cpf, email=email or '', password=cpf)
        # opcional: manter is_active=False até validação manual
        # user.is_active = False
        # user.save()

        aluno = form.save(commit=False)
        aluno.usuario = user
        aluno.save()

        messages.success(self.request, 'Cadastro de aluno realizado com sucesso. Faça login.')
        return redirect(self.success_url)


class ProfessorUserCreate(CreateView):
    model = Professor
    fields = ['nome', 'cpf', 'telefone', 'cidade']
    template_name = 'cadastros/registro/registro_professor.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        email = self.request.POST.get('email', '').strip()

        if User.objects.filter(username=cpf).exists():
            messages.error(self.request, 'Já existe um usuário com este CPF.')
            return self.form_invalid(form)

        user = User.objects.create_user(username=cpf, email=email or '', password=cpf)
        # opcional: user.is_active = False; user.save()

        professor = form.save(commit=False)
        professor.usuario = user
        professor.save()

        messages.success(self.request, 'Cadastro de professor realizado com sucesso. Faça login.')
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




